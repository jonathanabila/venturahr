from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from core.constants import NAMESPACE_CANDIDATE_PERMISSIONS
from opportunities.forms import OpportunityAnswersRequirementApplyForm
from opportunities.models import OpportunityAnswerRequirement, OpportunityRequirement


class OpportunitiesCandidateApplyView(PermissionRequiredMixin, generic.CreateView):
    form_class = OpportunityAnswersRequirementApplyForm
    queryset = OpportunityAnswerRequirement.objects

    template_name = "opportunities/privates/candidates/new.html"

    permission_required = NAMESPACE_CANDIDATE_PERMISSIONS

    def _build_context(self, request_post=None, queryset=None) -> dict:
        formset = modelformset_factory(
            OpportunityAnswerRequirement,
            form=OpportunityAnswersRequirementApplyForm,
            extra=0,
        )(request_post, queryset=queryset)

        return {"formset": formset}

    def get(self, request, *args, pk: int, **kwargs) -> HttpResponse:
        queryset = OpportunityRequirement.objects.filter(opportunity_id=pk)
        return render(request, self.template_name, self._build_context(queryset=queryset))

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        ...
