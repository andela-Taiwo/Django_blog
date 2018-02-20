from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from markdownx.utils import markdownify
from django.views.generic import View
from django.contrib.auth.models import User
from posts.models import Post
from .forms import CommentForm
# Create your views here.


class MessageView(View):
    pass
