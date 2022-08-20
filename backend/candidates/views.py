from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from candidates.forms import CandidatesRegistrationForm
from core.views import VenturaHRView


class CandidatesHomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "candidates/home.html"


class CandidatesLoginPageView(VenturaHRView, LoginView):
    template_name = "candidates/login.html"
    next_page = "candidates:home"


class CandidatesRegisterView(generic.CreateView):
    form_class = CandidatesRegistrationForm

    template_name = "candidates/register.html"
    success_url = reverse_lazy("candidates:login")
