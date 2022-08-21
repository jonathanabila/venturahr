from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from candidates.forms import CandidatesRegistrationForm
from core.views import VenturaHRView


class CandidatesHomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "candidates/home.html"


class CandidatesLoginPageView(VenturaHRView, LoginView):
    template_name = "candidates/login.html"
    next_page = "candidates:private-home"


class CandidatesRegisterView(VenturaHRView, generic.CreateView):
    form_class = CandidatesRegistrationForm

    template_name = "candidates/register.html"
    success_url = reverse_lazy("candidates:login")


class CandidatesPrivateHomePageView(
    VenturaHRView, PermissionRequiredMixin, generic.base.TemplateView
):
    template_name = "candidates/privates/home.html"

    permission_required = "candidates.view_candidate"
