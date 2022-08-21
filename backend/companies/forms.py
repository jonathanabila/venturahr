from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Permission
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from companies.models import Company, CompanyUser


class CompaniesAuthenticationForm(AuthenticationForm):
    company = forms.CharField(
        label=_("Company"),
        widget=forms.TextInput(),
    )


class CompaniesRegistrationForm(UserCreationForm):
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
            self.add_error("company", "Company not found!")
        return company_identifier

    def save(self, commit=True):
        """
        Adds the permission to view the private page from Company App.
        """
        with transaction.atomic():
            user = super().save(commit=True)

            # Adds the company
            company_identifier = self.cleaned_data.get("company")
            company = Company.objects.filter(identifier=company_identifier).first()
            user.company = company

            # Adds the permissions
            view_permissions = Permission.objects.filter(
                codename__in=("view_companyuser", "view_company")
            )
            user.user_permissions.add(*view_permissions)

            # Saves the changes
            user.save()

        return user
