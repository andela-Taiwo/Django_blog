from django.core.mail import send_mail
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.models import User
from posts.models import Post
from .forms import SignUpForm, ContactForm, LogInForm, PostForm


# Create your views here.

class PostView(View):
    template_name = 'posts.html'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get(self, request, *args, **kwargs):
        # <view logic>
        title = "Post a blog"
        form = PostForm(request.POST or None, request.FILES or
                        None)
        posts = Post.objects.all()
        # import pdb; pdb.set_trace()
        context = {
            'title': title,
            'posts': posts,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None, request.FILES or
                        None)
        if request.method == 'POST':
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.user_id = User.objects.get(pk=request.user.pk)
                post.save()
        return HttpResponseRedirect('/posts')


class PostUpdateView(View):
    template_name = 'post_edit.html'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def post(self, request, slug=None, *args, **kwargs):
        instance = get_object_or_404(Post, slug=slug)
        form = PostForm(request.POST or None, request.FILES or
                        None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/posts')

    def get(self, request, slug=None, *args, **kwargs):
        instance = get_object_or_404(Post, slug=slug)
        form = PostForm(request.POST or None, request.FILES or
                        None, instance=instance)
        context = {
            "title": instance.title,
            "form": form,
            }
        return render(request, self.template_name, context)


class PostDetailView(View):
    template_name = "post_detail.html"
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get(self, request, slug=None, *args, **kwargs):
            instance = get_object_or_404(Post, slug=slug)
            if instance:
                context = {
                    "title": instance.title,
                    "post": instance,
                    }
                return render(request, self.template_name, context)
            return HttpResponseRedirect('/posts')


class LoginView(View):
    template_name = 'login.html'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    print("I got here")
                    return HttpResponseRedirect('/posts')
                else:
                    return render(request, '<h3>Not active</h3>')

    def get(self, request, *args, **kwargs):
        #
        title = " DjangoCreek Login "
        form = LogInForm(request.POST or None)
        context = {
            "title": title,
            "form": form,
        }
        return render(request, self.template_name, context)


class SignUpView(View):
    template_name = 'signup.html'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def post(self, request, *args, **kwargs):

        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.email, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect('/posts')

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        title = "SignUp"
        context = {
            "title": title,
            "form": form,
        }
        return render(request, self.template_name, context)


class ContactView(View):
    template_name = 'contact.html'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            full_name = form.cleaned_data.get("full_name")
            message = form.cleaned_data.get("message")
            subject = form.cleaned_data.get("subject")
            try:
                send_mail(subject, message,
                          email,
                          ['sokunbimaimunah@gmail.com'], fail_silently=False)
            except ValueError:
                raise ValueError

        return HttpResponseRedirect('/contact')

    def get(self, request):
        form = ContactForm(request.POST or None)
        title = "Contact Us"
        context = {
            "title": title,
            "form": form,
        }

        return render(request, self.template_name, context)
