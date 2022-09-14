from django.views import generic

from core.constants import NAMESPACE_CANDIDATE_PERMISSIONS, NAMESPACE_RECRUITER_PERMISSIONS
from core.views import OrPermissionsRequiredMixin
from opportunities.constants import OPPORTUNITIES_PAGINATE_BY
from opportunities.models import Opportunity


class OpportunitiesOpportunityView(OrPermissionsRequiredMixin, generic.DetailView):
    model = Opportunity
    template_name = "opportunities/privates/view.html"

    permissions_required = (NAMESPACE_RECRUITER_PERMISSIONS, NAMESPACE_CANDIDATE_PERMISSIONS)


class OpportunitiesRecruiterOpportunities(OrPermissionsRequiredMixin, generic.ListView):
    model = Opportunity
    template_name = "opportunities/privates/list.html"

    queryset = Opportunity.objects.all().order_by("expires_at")
    paginate_by = OPPORTUNITIES_PAGINATE_BY

    permissions_required = (NAMESPACE_RECRUITER_PERMISSIONS, NAMESPACE_CANDIDATE_PERMISSIONS)
