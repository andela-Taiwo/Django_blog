from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from posts.views import (SignUpView, LoginView, ContactView, ProfileView)

urlpatterns = [
    url(r'^$', include('posts.urls')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^admin/', include(admin.site.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
