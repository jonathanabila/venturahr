from django.views import generic

from core.constants import (
    NAMESPACE_ADMIN_PERMISSIONS,
    NAMESPACE_CANDIDATE_PERMISSIONS,
    NAMESPACE_RECRUITER_PERMISSIONS,
)
from core.models import User
from core.views import OrPermissionsRequiredMixin
from opportunities.constants import OPPORTUNITIES_PAGINATE_BY
from opportunities.models import Opportunity


class OpportunitiesOpportunityView(OrPermissionsRequiredMixin, generic.DetailView):
    model = Opportunity
    template_name = "opportunities/privates/view.html"

    permissions_required = (
        NAMESPACE_RECRUITER_PERMISSIONS,
        NAMESPACE_CANDIDATE_PERMISSIONS,
        NAMESPACE_ADMIN_PERMISSIONS,
    )

    def get_context_data(self, **kwargs) -> dict:
        user: User = self.request.user
        return {**super().get_context_data(**kwargs), "can_apply": user.can_apply(self.object.id)}


class OpportunitiesRecruiterOpportunities(OrPermissionsRequiredMixin, generic.ListView):
    model = Opportunity
    # TODO: When a candidate clicks on Opportunities, it redirected to company opportunities,
    #  which it isn't the goal.
    template_name = "opportunities/privates/list.html"

    queryset = Opportunity.objects.all().order_by("expires_at")
    paginate_by = OPPORTUNITIES_PAGINATE_BY

    permissions_required = (
        NAMESPACE_RECRUITER_PERMISSIONS,
        NAMESPACE_CANDIDATE_PERMISSIONS,
        NAMESPACE_ADMIN_PERMISSIONS,
    )
