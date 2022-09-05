from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views import generic

from core.constants import NAMESPACE_RECRUITER_PERMISSIONS
from opportunities.forms import OpportunityNewForm
from opportunities.models import Opportunity


class OpportunitiesNewOpportunityView(PermissionRequiredMixin, generic.CreateView):
    form_class = OpportunityNewForm
    queryset = Opportunity.objects

    template_name = "opportunities/privates/new.html"

    permission_required = NAMESPACE_RECRUITER_PERMISSIONS

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"current_user": self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, current_user=request.user, **kwargs)

    def get_success_url(self):
        return reverse("opportunities:private-opportunity", kwargs={"pk": self.object.id})


class OpportunitiesRecruiterOpportunityView(PermissionRequiredMixin, generic.DetailView):
    model = Opportunity
    template_name = "opportunities/privates/view.html"

    permission_required = NAMESPACE_RECRUITER_PERMISSIONS


class OpportunitiesRecruiterOpportunities(PermissionRequiredMixin, generic.ListView):
    model = Opportunity

    template_name = "opportunities/privates/list.html"

    permission_required = NAMESPACE_RECRUITER_PERMISSIONS
