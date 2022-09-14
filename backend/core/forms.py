from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Model
from django.forms import BaseModelFormSet, ModelForm

from .models import User


class BaseFormWithWidgets(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args, **{**kwargs, "use_required_attribute": True, "empty_permitted": False}
        )
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(
        max_length=30,
        required=True,
    )
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class EmptyFormset(BaseModelFormSet):
    object_to_overide_queryset: Model = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, "queryset": None})
        self.queryset = self.object_to_overide_queryset
