from django.db import transaction
from django.forms import BaseModelFormSet

from core.metrics import add_opportunity_counter, add_opportunity_requirements_counter
from opportunities.forms import OpportunityNewForm
from opportunities.models import Opportunity, OpportunityAnswer


class OpportunityService:
    @staticmethod
    def is_valid(opportunityform: OpportunityNewForm, formset: BaseModelFormSet) -> bool:
        return opportunityform.is_valid() and formset.is_valid()

    @staticmethod
    def create_opportunity_with_requirements(
        opportunityform: OpportunityNewForm, formset: BaseModelFormSet
    ) -> Opportunity:
        with transaction.atomic():
            opportunity = opportunityform.save()

            for requirement in formset:
                requirement.save(opportunity, opportunity.created_by)

        add_opportunity_counter().inc()
        add_opportunity_requirements_counter().inc(len(formset))
        return opportunity


class OpportunityAnswerService:
    @staticmethod
    def create_answers_requirement(
        opportunity_pk: int, user, formset: BaseModelFormSet, *args, **kwargs
    ) -> OpportunityAnswer:
        with transaction.atomic():
            opportunity = Opportunity.objects.get(id=opportunity_pk)

            for answer_requirement in formset:
                opportunity_answer, _ = answer_requirement.save(
                    opportunity, answer_requirement.initial["opportunity_requirement_id"], user
                )

        return opportunity_answer
