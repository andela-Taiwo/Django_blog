from django import forms
from .models import User, Post


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


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")
        return content


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        print(email)
        return email
