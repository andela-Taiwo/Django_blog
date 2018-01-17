from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm, SignInForm


# Create your views here.
def home(request):

    title = " DjangoCreek SignIn "
    form = SignInForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
        "STATIC_URL": settings.STATIC_URL
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.email = form.cleaned_data.get('email')
        if instance.email:
            instance.save()
        context = {
            "title": "Thank You"
        }
    return render(request, 'index.html', context)


def register(request):

    title = " Welcome to Django creek {}" .format(request.user)
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
        "STATIC_URL": settings.STATIC_URL
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.email = form.cleaned_data.get('email')
        if instance.email:
            instance.save()
        context = {
            "title": "Thank You",
            "STATIC_URL": settings.STATIC_URL
        }
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form,
        "STATIC_URL": settings.STATIC_URL
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get("full_name")
        context = {
            "STATIC_URL": settings.STATIC_URL,
            "title": "Thank You"
        }
        try:
            send_mail('Subject here', 'Here is the message.',
                      'sokunbimaimunah@gmail.com',
                      ['sokunbimaimunah@gmail.com'], fail_silently=False)
            print("yay workd")
        except ValueError:
            raise ValueError

    return render(request, 'index.html', context)
