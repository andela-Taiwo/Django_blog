from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Post
from .forms import SignUpForm, ProfileForm


# admin.site.unregister(User)
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_form = ProfileForm
    form = SignUpForm
    list_display = (
        'email', 'admin',
    )

    # fieldsets = (
    #     ('Account', {'fields': ('email', 'admin')}),
    #     ('Personal info', {'fields': (
    #         'first_name', 'last_name',
    #         )}),
    # )

    ordering = (
        'email',
    )

    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name'), }),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    filter_horizontal = ()


class PostsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user_id",
                    "date_created", "date_updated", "publish"]


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostsAdmin)
