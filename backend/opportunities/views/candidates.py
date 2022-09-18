from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from core.constants import NAMESPACE_CANDIDATE_PERMISSIONS
from opportunities.forms import OpportunityAnswerRequirementApplyForm
from opportunities.models import OpportunityAnswerRequirement, OpportunityRequirement
from opportunities.services import OpportunityAnswerService


class OpportunitiesCandidateApplyView(PermissionRequiredMixin, generic.CreateView):
    form_class = OpportunityAnswerRequirementApplyForm
    queryset = OpportunityAnswerRequirement.objects

    template_name = "opportunities/privates/applications/new.html"

    permission_required = NAMESPACE_CANDIDATE_PERMISSIONS

    opportunity_answer_service = OpportunityAnswerService()

    def _build_context(self, opportunity_id: int, request_post=None) -> dict:
        initial = [
            {k: getattr(r, f) for k, f in self.form_class.Meta.map.items()}
            for r in OpportunityRequirement.objects.filter(opportunity_id=opportunity_id)
        ]

        formset = modelformset_factory(
            OpportunityAnswerRequirement,
            form=OpportunityAnswerRequirementApplyForm,
            extra=len(initial),
            can_delete_extra=False,
            can_delete=False,
        )(request_post, queryset=self.queryset.none(), initial=initial)

        return {"formset": formset}

    def get(self, request, *args, pk: int, **kwargs) -> HttpResponse:
        return render(request, self.template_name, self._build_context(pk))

    def post(self, request, *args, pk: int, **kwargs) -> HttpResponseRedirect:
        context = self._build_context(pk, request_post=request.POST)

        if not context["formset"].is_valid():
            return render(request, self.template_name, context)

        _ = self.opportunity_answer_service.create_answers_requirement(
            pk, self.request.user, **context
        )

        return HttpResponseRedirect(reverse("opportunities:private-opportunities"))
