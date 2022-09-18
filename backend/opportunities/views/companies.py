from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from core.constants import NAMESPACE_RECRUITER_PERMISSIONS
from core.views import GenericCreateViewWithUser, VenturaHRView
from opportunities.constants import CANDIDATES_PAGINATE_BY
from opportunities.forms import (
    OpportunityNewForm,
    OpportunityRequirementEmptyFormset,
    OpportunityRequirementNewForm,
)
from opportunities.models import Opportunity, OpportunityAnswer, OpportunityRequirement
from opportunities.services import OpportunityService


class OpportunitiesNewOpportunityView(
    VenturaHRView, PermissionRequiredMixin, GenericCreateViewWithUser
):
    form_class = OpportunityNewForm
    queryset = Opportunity.objects

    template_name = "opportunities/privates/new.html"

    permission_required = NAMESPACE_RECRUITER_PERMISSIONS

    opportunity_service = OpportunityService()

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

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name, self._build_context())

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        context = self._build_context(request.POST)
        if not self.opportunity_service.is_valid(**context):
            return render(request, self.template_name, context)

        opportunity = self.opportunity_service.create_opportunity_with_requirements(**context)

        return HttpResponseRedirect(
            reverse("opportunities:private-opportunity", kwargs={"pk": opportunity.id})
        )


class OpportunityCandidatesView(VenturaHRView, generic.ListView):
    opportunity_id: int

    model = OpportunityAnswer

    template_name = "opportunities/privates/candidates/list.html"
    permission_required = NAMESPACE_RECRUITER_PERMISSIONS
    paginate_by = CANDIDATES_PAGINATE_BY

    def get_queryset(self):
        return OpportunityAnswer.objects.filter(opportunity_id=self.opportunity_id).all()

    def get(self, request, *args, pk: int, **kwargs):
        self.opportunity_id = pk
        return super().get(request, *args, **kwargs)
