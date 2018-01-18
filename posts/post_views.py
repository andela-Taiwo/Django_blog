from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from posts.models import Post


class MyView(View):
    def get(self, request):
        # <view logic>
        posts = Post.objects.all()
        return HttpResponse('result', posts)
