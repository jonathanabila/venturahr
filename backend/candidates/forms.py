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
            view_candidate_permission = Permission.objects.get(codename="view_candidate")
            user.user_permissions.add(view_candidate_permission)

        return user
