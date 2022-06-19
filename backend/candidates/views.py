from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic

from core.views import VenturaHRView


class CandidateHomePageView(VenturaHRView, PermissionRequiredMixin, generic.base.TemplateView):
    template_name = "candidates/home.html"
    permission_required = ("candidates.view",)
