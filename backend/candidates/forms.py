from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.db import transaction

from candidates.models import CandidateUser


class CandidatesRegistrationForm(UserCreationForm):
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
                codename__in=("view_candidateuser", "change_candidateuser")
            )
            user.user_permissions.add(*candidate_permissions)

            # Saves the changes
            user.save()

        return user


class CandidateUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CandidateUser
        fields = ("username", "first_name", "last_name", "email")

    username = forms.CharField(disabled=True)
    first_name = forms.CharField(disabled=True)
    last_name = forms.CharField(disabled=True)
