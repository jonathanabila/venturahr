import logging
from abc import ABC

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View, generic

from core.forms import SignUpForm

logger = logging.getLogger(__name__)


class VenturaHRView(ABC, View):
    ...


class HomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "core/home.html"


class VenturaHRRegisterView(generic.CreateView):
    form_class = SignUpForm

    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")


class VenturaHRLoginView(LoginView):
    template_name = "login.html"


class VenturaHRLoginRequiredView(LoginRequiredMixin, VenturaHRView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
