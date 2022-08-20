from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from companies.forms import CompaniesAuthenticationForm, CompaniesRegistrationForm
from core.views import VenturaHRView


class CompaniesHomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "companies/home.html"


class CompaniesLoginView(LoginView):
    form_class = CompaniesAuthenticationForm

    template_name = "companies/login.html"
    next_page = "companies:home"


class CompaniesRegisterView(generic.CreateView):
    form_class = CompaniesRegistrationForm

    template_name = "companies/register.html"
    success_url = reverse_lazy("companies:login")
