from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "full_name", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name
