from django.contrib.auth.views import LoginView
from django.views import generic

from core.views import VenturaHRView


class CompanyHomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "companies/home.html"


class CompanyLoginView(LoginView):
    template_name = "login.html"
