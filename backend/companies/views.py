from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views import generic

from companies.forms import (
    CompaniesAuthenticationForm,
    CompaniesRecruiterRegistrationForm,
    CompaniesRegistrationForm,
    CompanyUserUpdateForm,
)
from companies.models import CompanyUser
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


class CompaniesPrivateHomePageView(
    VenturaHRView, PermissionRequiredMixin, generic.base.TemplateView
):
    template_name = "companies/privates/home.html"

    permission_required = "companies.view_companyuser"


class CompaniesNewRecruiterView(generic.CreateView):
    form_class = CompaniesRecruiterRegistrationForm

    template_name = "companies/privates/new_recruiter.html"
    success_url = reverse_lazy("companies:private-home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"current_user": self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, current_user=request.user, **kwargs)


class CompaniesPrivateEditView(PermissionRequiredMixin, generic.edit.UpdateView):
    form_class = CompanyUserUpdateForm
    queryset = CompanyUser.objects

    template_name = "companies/privates/edit.html"

    permission_required = ("companies.change_companyuser", "companies.change_companyrecruiteruser")

    def get_success_url(self):
        return reverse("companies:private-home")
