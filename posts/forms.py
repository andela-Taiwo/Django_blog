from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template.defaultfilters import slugify
from markdownx.fields import MarkdownxFormField
from .models import Post, Profile
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2",
                  "username", "birth_date"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        return first_name

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        return password2

    def clean_user_name(self):
        username = self.cleaned_data.get("username")
        return username


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username

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

    # def save(self):
    #     instance = super().save(commit=False)
    #
    #     max_length = Post._meta.get_field('slug').max_length
    #     instance.slug = orig = slugify(instance.title)[:max_length]
    #
    #     for x in itertools.count(1):
    #         if not Post.objects.filter(slug=instance.slug).exists():
    #             break
    #
    #         # Truncate the original slug dynamically. Minus 1 for the hyphen.
    #         instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
    #
    #     instance.save()
    #
    #     return instance


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
