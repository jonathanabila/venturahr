from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from core.constants import NAMESPACE_RECRUITER_PERMISSIONS
from opportunities.forms import (
    OpportunityNewForm,
    OpportunityRequirementEmptyFormset,
    OpportunityRequirementNewForm,
)
from opportunities.models import Opportunity, OpportunityRequirement
from opportunities.services import OpportunityService


class OpportunitiesNewOpportunityView(PermissionRequiredMixin, generic.CreateView):
    form_class = OpportunityNewForm
    queryset = Opportunity.objects

    template_name = "opportunities/privates/new.html"

    permission_required = NAMESPACE_RECRUITER_PERMISSIONS

    opportunity_service = OpportunityService()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"current_user": self.request.user})
        return kwargs

    def _build_context(self, data=None) -> dict:
        formset = modelformset_factory(
            OpportunityRequirement,
            form=OpportunityRequirementNewForm,
            formset=OpportunityRequirementEmptyFormset,
        )(data)

        return {
            "opportunityform": OpportunityNewForm(data, current_user=self.request.user),
            "formset": formset,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self._build_context())

    def post(self, request, *args, **kwargs):
        context = self._build_context(request.POST)
        if not self.opportunity_service.is_valid(**context):
            return render(request, self.template_name, context)

        opportunity = self.opportunity_service.create_opportunity_with_requirements(**context)

        return HttpResponseRedirect(
            reverse("opportunities:private-opportunity", kwargs={"pk": opportunity.id})
        )
