from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import Post
from .models import User


class SignUserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "full_name", "date_created"]
    readonly_fields = ('id',)
    form = SignUpForm
    # class meta:
    #     User


class PostsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user_id", "slug", "date_created", "date_updated"]


admin.site.register(User, SignUserAdmin)
admin.site.register(Post, PostsAdmin)
