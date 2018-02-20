from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from posts.views import *

urlpatterns = [
    url(r'^$', MessageView.as_view(), name='posts'),
    url(r'^/edit$', MessageView.as_view(), name='posts'),
    ]
