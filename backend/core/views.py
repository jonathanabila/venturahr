import logging
from abc import ABC
from typing import Tuple

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LogoutView
from django.core.exceptions import ImproperlyConfigured
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.base import ContextMixin
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class VenturaHRView(ABC, ContextMixin, APIView):
    def dispatch(self, request, *args, **kwargs) -> HttpResponseRedirectBase:
        # If private is the path, and we redirect, we'll have a nice loop
        if (
            (user := request.user)
            and user.is_authenticated
            and not any(r in request.path for r in ["private", "logout"])
        ):
            if user.company:
                return redirect("companies:private-home")
            else:
                return redirect("candidates:private-home")
        return super().dispatch(request, *args, **kwargs)


class HomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "core/home.html"


class VenturaHRLogoutView(VenturaHRView, LogoutView):
    next_page = "core:home"


class OrPermissionsRequiredMixin(PermissionRequiredMixin):
    permissions_required: Tuple[Tuple[str, ...], ...]

    def has_permission(self):
        if self.permission_required:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} has .permission_required. Define .permission_required "
                "or use PermissionRequiredMixin directly."
            )

        if self.permissions_required is None:
            return super().has_permission()

        return any(self.request.user.has_perms(p) for p in self.permissions_required)


class GenericCreateViewWithUser(generic.CreateView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"current_user": self.request.user})
        return kwargs
