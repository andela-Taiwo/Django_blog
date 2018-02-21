from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from posts.views import PostView, PostUpdateView, PostDetailView

urlpatterns = [
    url(r'^$', PostView.as_view(), name='posts'),
    url(r'^(?P<slug>[\w-]+)/edit/$',
        login_required(PostUpdateView.as_view()), name='post_update'),
    url(r'^(?P<slug>[\w-]+)/$',
        PostDetailView.as_view(), name='post_detail'),
]
