import datetime
from typing import Union

from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms import BaseModelFormSet, ModelForm
from django.utils import timezone

from companies.models import CompanyRecruiterUser, CompanyUser
from core.constants import MAXIMUM_OPPORTUNITY_INTERVAL, MINIMUM_OPPORTUNITY_INTERVAL
from core.models import User
from opportunities.models import Opportunity, OpportunityRequirement


class OpportunityNewForm(ModelForm):
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
                f"An Opportunity has to last at last for {MINIMUM_OPPORTUNITY_INTERVAL} days."
            )

        return expires_at


class OpportunityRequirementNewForm(ModelForm):
    instance: OpportunityRequirement

    class Meta:
        model = OpportunityRequirement
        fields = ["name", "description", "weight"]

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        required=True,
    )

    def save(
        self, opportunity: Opportunity, created_by: User, commit=True
    ) -> OpportunityRequirement:
        with transaction.atomic():
            self.instance.company = opportunity.company
            self.instance.opportunity = opportunity
            self.instance.created_by = created_by

            requirement = super().save(commit=commit)

        return requirement


class OpportunityRequirementEmptyFormset(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "queryset": None})
        self.queryset = OpportunityRequirement.objects.none()
