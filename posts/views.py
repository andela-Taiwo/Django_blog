from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from posts.models import Post, User
from .forms import SignUpForm, ContactForm, SignInForm, PostForm


# Create your views here.

class MyView(View):
    template_name = 'posts.html'
    STATIC_URL = settings.STATIC_URL

    def get(self, request, *args, **kwargs):
        # <view logic>
        title = "Post a blog"
        form = PostForm(request.POST or None)
        posts = Post.objects.all()
        context = {
            'title': title,
            'form': form,
            'posts': posts,
            'STATIC_URL': self.STATIC_URL
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        title = "Blog suceessfully posted"
        form = PostForm(request.POST or None)
        # import pdb; pdb.set_trace
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.user_id = User.objects.get(pk=request.user.pk)
            post.save()

        context = {
            'title': title,
            'STATIC_URL': settings.STATIC_URL
        }
        return render(request, 'posts.html', context)


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
