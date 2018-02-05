from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Post


class PostsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user_id", "slug",
                    "date_created", "date_updated", "publish"]


admin.site.register(Post, PostsAdmin)
