from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from markdownx.utils import markdownify
from django.views.generic import View
from .models import User
# from notification.models import Notification
from notifications.signals import notify
from posts.models import Post
from comments.models import Comment
from .forms import SignUpForm, ContactForm, LogInForm, PostForm, ProfileForm
from comments.forms import CommentForm


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
        for post in posts:
            post.content = markdownify(post.content)
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
                # import pdb; pdb.set_trace()
                post.author = request.user
                post.user_id_id = User.objects.get(pk=request.user.pk).pk
                post.save()
        return HttpResponseRedirect('/')


class PostUpdateView(View):
    template_name = 'post_edit.html'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    # @login_required
    def post(self, request, slug=None, *args, **kwargs):
        instance = get_object_or_404(Post, slug=slug)
        form = PostForm(request.POST or None, request.FILES or
                        None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    # @login_required
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
            post = get_object_or_404(Post, slug=slug)
            post.content = markdownify(post.content)
            comment_form = CommentForm(request.POST or None)
            comment = Comment.objects.filter(post=post.id)
            if post:
                context = {
                    "title": post.title,
                    "post": post,
                    "form": comment_form,
                    "comments": comment,

                    }
                return render(request, self.template_name, context)
            return HttpResponseRedirect('/')

    def post(self, request, slug=None, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        # import pdb;pdb.set_trace()
        if request.method == 'POST':
            comment_form = CommentForm(request.POST or None)
            if comment_form.is_valid() and request.user.is_authenticated():
                # content = comment_form.clean_message()
                temp = comment_form.save(commit=False)
                parent = comment_form['parent'].value()
                content_data = comment_form.clean_message()
                user1 = User.objects.filter(id=post.user_id.id)
                if parent == '':
                    # Set a blank path then save it to get an ID
                    temp.path = []
                    temp.author = request.user
                    temp.post = post
                    temp.save()

                    temp.path = [temp.id]
                    notify.send(request.user, recipient=user1,
                                verb='Post comment', action_object=post)
                else:
                    # Get the parent node
                    node = Comment.objects.filter(id=parent)
                    if node.exists() and node.count() == 1:
                        node = node.first()
                    temp.depth = node.depth + 1
                    temp.path = node.path
                    temp.author = request.user
                    temp.post = post
                    # Store parents path then apply comment ID
                    temp.save()
                    temp.path.append(temp.id)
                    notify.send(request.user, recipient=user1,
                                verb='You have reply on your comment')

                # Final save for parents and children
                temp.save()
        comments = Comment.objects.all().order_by('path')
        return HttpResponseRedirect('/{0}'.format(post.slug))


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
                    return HttpResponseRedirect('/')
                else:
                    return render(request, '<h3>Not active</h3>')
            return HttpResponseRedirect('/')

    def get(self, request, *args, **kwargs):
        #
        title = " DjangoCreek Login "
        form = LogInForm()
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
            auth_login(request, user)
        return HttpResponseRedirect('/')

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        title = "SignUp"
        context = {
            "title": title,
            "form": form,
        }
        return render(request, self.template_name, context)


class ProfileView(View):
    template_name = 'profile.html'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get(self, request, *args, **kwargs):
        user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }
        return render(request, self.template_name, context)

    def post(self, request,  *args, **kwargs):
        if request.method == 'POST':
            user_form = SignUpForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST,
                                       request.FILES or None,
                                       instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your profile was successfully updated!')

            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please correct the error below')
            return HttpResponseRedirect('/')


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
