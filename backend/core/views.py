import logging
from abc import ABC

from django.contrib.auth.views import LogoutView
from django.views import View, generic

logger = logging.getLogger(__name__)


class VenturaHRView(ABC, View):
    ...


class HomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "core/home.html"


class VenturaHRLogoutView(VenturaHRView, LogoutView):
    next_page = "core:home"
