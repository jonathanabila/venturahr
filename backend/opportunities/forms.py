import datetime
from typing import Tuple, Union

from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Model
from django.utils import timezone

from companies.models import CompanyRecruiterUser, CompanyUser
from core.constants import MAXIMUM_OPPORTUNITY_INTERVAL, MINIMUM_OPPORTUNITY_INTERVAL
from core.forms import BaseFormWithWidgets, EmptyFormset
from core.models import User
from opportunities.models import (
    Opportunity,
    OpportunityAnswer,
    OpportunityAnswerRequirement,
    OpportunityRequirement,
)


class OpportunityNewForm(BaseFormWithWidgets):
    instance: Opportunity

    def __init__(self, *args, current_user, **kwargs) -> None:
        self.current_user: Union[CompanyRecruiterUser, CompanyUser] = current_user
        super().__init__(*args, **kwargs)

    class Meta:
        model = Opportunity
        fields = ["name", "description", "expires_at"]

    expires_at = forms.DateField(
        initial=datetime.date.today, widget=forms.DateInput(format="%Y-%m-%d")
    )

    def save(self, commit=True) -> Opportunity:
        with transaction.atomic():
            self.instance.company = self.current_user.company
            self.instance.created_by = self.current_user

            opportunity = super().save(commit=commit)

        return opportunity

    def clean_expires_at(self):
        expires_at = self.cleaned_data["expires_at"]

        if (expires_at - timezone.now().date()) > datetime.timedelta(
            days=MAXIMUM_OPPORTUNITY_INTERVAL
        ):
            raise ValidationError(
                f"An Opportunity can only last for {MAXIMUM_OPPORTUNITY_INTERVAL} days."
            )

        if (expires_at - timezone.now().date()) < datetime.timedelta(
            days=MINIMUM_OPPORTUNITY_INTERVAL
        ):
            raise ValidationError(
                f"An Opportunity has to last at least for {MINIMUM_OPPORTUNITY_INTERVAL} days."
            )

        return expires_at


class OpportunityRequirementNewForm(BaseFormWithWidgets):
    instance: OpportunityRequirement

    class Meta:
        model = OpportunityRequirement
        fields = ["name", "description", "weight", "minimim_knowledge"]

    name = forms.CharField()
    weight = forms.IntegerField(min_value=1, max_value=5)
    minimim_knowledge = forms.IntegerField(label="PMD", min_value=1, max_value=5)

    def save(
        self, opportunity: Opportunity, created_by: User, commit=True
    ) -> OpportunityRequirement:
        with transaction.atomic():
            self.instance.company = opportunity.company
            self.instance.opportunity = opportunity
            self.instance.created_by = created_by

            requirement = super().save(commit=commit)

        return requirement


class OpportunityRequirementEmptyFormset(EmptyFormset):
    object_to_overide_queryset: Model = OpportunityRequirement.objects.none()


class OpportunityAnswerRequirementApplyForm(BaseFormWithWidgets):
    instance: OpportunityAnswerRequirement

    class Meta:
        model = OpportunityAnswerRequirement
        fields = ["name", "description", "answer"]
        map = {"name": "name", "description": "description", "opportunity_requirement_id": "id"}

    name = forms.CharField(label="", widget=forms.TextInput(attrs={"readonly": "readonly"}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={"readonly": "readonly"}))

    answer = forms.IntegerField(min_value=1, max_value=5)
    opportunity_requirement_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    field_order = ["name", "description", "answer"]

    def save(
        self,
        opportunity: Opportunity,
        opportunity_requirement_id: int,
        created_by: User,
        commit=True,
    ) -> Tuple[OpportunityAnswer, OpportunityAnswerRequirement]:
        with transaction.atomic():
            opportunity_answer, _ = OpportunityAnswer.objects.get_or_create(
                opportunity=opportunity,
                created_by=created_by,
            )

            self.instance.created_by = created_by
            self.instance.opportunity_answer = opportunity_answer
            self.instance.opportunity_requirement_id = opportunity_requirement_id

            answer_requirement = super().save(commit=commit)

        return opportunity_answer, answer_requirement


class OpportunityAnswerRequirementViewForm(OpportunityAnswerRequirementApplyForm):
    answer = forms.IntegerField(
        min_value=1, max_value=5, widget=forms.TextInput(attrs={"readonly": "readonly"})
    )
