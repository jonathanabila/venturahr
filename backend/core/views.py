import logging
from abc import ABC

from django.contrib.auth.views import LogoutView
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class VenturaHRView(ABC, TemplateView):
    def dispatch(self, request, *args, **kwargs) -> HttpResponseRedirectBase:
        # If private is the path, and we redirect, we'll have a nice loop
        if (user := request.user) and user.is_authenticated and "private" not in request.path:
            if user.company:
                return redirect("companies:private-home")
            else:
                return redirect("candidates:private-home")
        return super().dispatch(request, *args, **kwargs)


class HomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "core/home.html"


class VenturaHRLogoutView(VenturaHRView, LogoutView):
    next_page = "core:home"
