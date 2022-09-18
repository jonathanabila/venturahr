import logging

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Permission
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from companies.models import Company, CompanyRecruiterUser, CompanyUser
from core.constants import RECRUITER_PERMISSIONS
from core.forms import BaseFormWithWidgets

logger = logging.getLogger(__name__)


class CompaniesAuthenticationForm(AuthenticationForm):
    company = forms.CharField(
        label=_("Company"),
        widget=forms.TextInput(),
    )


class CompaniesRegistrationForm(BaseFormWithWidgets, UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=50, required=True)

    company = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CompanyUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def clean_company(self) -> str:
        company_identifier = self.cleaned_data.get("company")
        company = Company.objects.filter(identifier=company_identifier).first()
        if not company:
            logger.debug(f"Company [{company}] not found, skipping validation")
        return company_identifier

    def save(self, commit=True):
        """
        Adds the permission to view the private page from Company App.
        """
        with transaction.atomic():
            user = super().save(commit=True)

            # Adds the company
            company_identifier = self.cleaned_data.get("company")
            company, _ = Company.objects.get_or_create(
                identifier=company_identifier, name=company_identifier
            )
            user.company = company

            # Adds the permissions
            view_permissions = Permission.objects.filter(
                codename__in=(
                    # Company
                    "view_companyuser",
                    "view_company",
                    "change_companyuser",
                    "change_companyrecruiteruser",
                    "add_companyrecruiteruser",
                    "delete_companyrecruiteruser",
                    # Opportunities
                    "view_opportunity",
                )
            )
            user.user_permissions.add(*view_permissions)

            # Saves the changes
            user.save()

        return user


class CompaniesRecruiterRegistrationForm(BaseFormWithWidgets, UserCreationForm):
    def __init__(self, *args, current_user, **kwargs):
        self.current_user = current_user
        super().__init__(*args, **kwargs)

    class Meta:
        model = CompanyRecruiterUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        """
        Adds the permission to view the private page from Company App.
        """
        with transaction.atomic():
            user = super().save(commit=True)

            # Adds the company
            user.company = self.current_user.company

            # Adds the permissions
            view_permissions = Permission.objects.filter(
                codename__in=(
                    # Company
                    "view_companyuser",
                    "view_company",
                    "change_companyuser",
                    "change_companyrecruiteruser",
                    # Opportunity
                    *RECRUITER_PERMISSIONS,
                )
            )
            user.user_permissions.add(*view_permissions)

            # Saves the changes
            user.save()

        return user


class CompanyUserUpdateForm(BaseFormWithWidgets):
    class Meta:
        model = CompanyUser
        fields = ("username", "first_name", "last_name", "email")

    username = forms.CharField(disabled=True)
    first_name = forms.CharField(disabled=True)
    last_name = forms.CharField(disabled=True)
