from django import forms

from .models import Password


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ["title", "password"]
        labels = {
            "title": "Title",
            "password": "Password",
        }
        widgets = {
            "password": forms.TextInput(
                attrs={"placeholder": "Password", "required": "required"}
            ),
            "title": forms.TextInput(
                attrs={"placeholder": "Title", "required": "required"}
            ),
        }
