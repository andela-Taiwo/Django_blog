from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm


# Create your views here.
def home(request):

    title = " Welcome to Django creek {}" .format(request.user)
    # import pdb; pdb.set_trace()
    form = SignUpForm(request.POST or None)
    print(form)
    context = {
        "title": title,
        "form": form
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


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get("full_name")
        context = {
            "title": "Thank You"
        }
        send_mail('Subject here', 'Here is the message.',
                  settings.EMAIL_HOST_USER,
                  ['sokunbimaimunah@gmail.com'], fail_silently=False)
    return render(request, 'index.html', context)
