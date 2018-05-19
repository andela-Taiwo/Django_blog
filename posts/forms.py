from django import forms
from django.contrib.auth import hashers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from markdownx.fields import MarkdownxFormField
from .models import Post, Profile
from .models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', "birth_date", 'first_name', 'last_name',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    # class Meta:
    #     model = User
    #     password1 = forms.CharField(
    #         widget=forms.PasswordInput)
    #     password2 = forms.CharField(
    #         label='Confirm password',
    #         help_text=_("Enter the same password as before, for \
    #                      verification."),
    #         widget=forms.PasswordInput)
    #     fields = ["email", "first_name", "last_name", "password1", "password2",
    #               "username", "birth_date"]
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     return email
    #
    # def clean_last_name(self):
    #     last_name = self.cleaned_data.get("last_name")
    #     return last_name
    #
    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get("first_name")
    #     return first_name
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     return password1
    #
    # def clean_password2(self):
    #     password2 = self.cleaned_data.get("password2")
    #     return password2
    #
    # def clean_user_name(self):
    #     username = self.cleaned_data.get("username")
    #     return username


class LogInForm(AuthenticationForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ["email", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def password(self):
        password = self.cleaned_data.get("password")
        return password


class PostForm(forms.ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = Post
        fields = ["title", "content", "blog_image"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")
        return content


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        print(email)
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', 'gender')
