from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.db import transaction

from candidates.models import CandidateUser
from core.constants import CANDIDATE_PERMISSIONS
from core.forms import BaseFormWithWidgets


class CandidatesRegistrationForm(BaseFormWithWidgets, UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = CandidateUser
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
        Adds the permission to view the private page from Candidates App.
        """
        with transaction.atomic():
            user = super().save(commit=True)

            # Adds the permissions
            candidate_permissions = Permission.objects.filter(
                codename__in=(
                    "view_candidateuser",
                    "change_candidateuser",
                    # Opportunity
                    *CANDIDATE_PERMISSIONS,
                )
            )
            user.user_permissions.add(*candidate_permissions)

            # Saves the changes
            user.save()

        return user


class CandidateUserUpdateForm(BaseFormWithWidgets):
    class Meta:
        model = CandidateUser
        fields = ("username", "first_name", "last_name", "email")

    username = forms.CharField(disabled=True)
    first_name = forms.CharField(disabled=True)
    last_name = forms.CharField(disabled=True)
