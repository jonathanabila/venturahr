from django.db import transaction
from django.forms import BaseModelFormSet

from opportunities.forms import OpportunityNewForm
from opportunities.models import Opportunity


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

        return opportunity
