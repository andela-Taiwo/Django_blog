from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from posts.views import MyView, post_update

urlpatterns = [
    url(r'^$', include('posts.urls')),
    url(r'^signin/$', 'posts.views.home', name='home'),
    url(r'^posts/', include('posts.urls')),
    url(r'^posts/(?P<id>[0-9]+)/edit/$', 'posts.views.post_update', name='update'),
    url(r'^posts/(?P<id>[0-9]+)/detail/$', 'posts.views.post_detail', name='detail'),
    url(r'^$register/$', 'posts.views.register', name='register'),
    url(r'^contact/$', 'posts.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
