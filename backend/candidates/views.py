from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views import generic

from candidates.forms import CandidatesRegistrationForm, CandidateUserUpdateForm
from candidates.models import CandidateUser
from core.views import VenturaHRView


class CandidatesHomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "candidates/home.html"


class CandidatesLoginPageView(VenturaHRView, LoginView):
    template_name = "candidates/login.html"
    next_page = "candidates:private-home"


class CandidatesRegisterView(generic.CreateView):
    form_class = CandidatesRegistrationForm

    template_name = "candidates/register.html"
    success_url = reverse_lazy("candidates:login")


class CandidatesPrivateHomePageView(
    VenturaHRView, PermissionRequiredMixin, generic.base.TemplateView
):
    template_name = "candidates/privates/home.html"

    permission_required = "candidates.view_candidateuser"


class CandidatesPrivateEditView(PermissionRequiredMixin, generic.edit.UpdateView):
    form_class = CandidateUserUpdateForm
    queryset = CandidateUser.objects

    template_name = "candidates/privates/edit.html"

    permission_required = ("candidates.view_candidateuser", "candidates.change_candidateuser")

    def get_success_url(self):
        return reverse("candidates:private-home")
