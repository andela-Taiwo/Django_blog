from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'posts.views.home', name='home'),
    # url(r'^posts/$', MyView.as_view(), name='posts'),
    url(r'^posts/', include('posts.urls')),
    url(r'^$register/$', 'posts.views.register', name='register'),
    url(r'^contact/$', 'posts.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
