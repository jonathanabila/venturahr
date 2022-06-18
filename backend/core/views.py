import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views import View, generic

logger = logging.getLogger(__name__)


class VenturaHRView(View):
    ...


class HomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "core/home.html"


class VenturaHRLoginView(LoginView):
    template_name = "login.html"


class VenturaHRLoginRequiredView(LoginRequiredMixin, VenturaHRView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
