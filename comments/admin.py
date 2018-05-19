from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'message', 'author', 'date_created'
    ]

    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(approval='AP')
    make_published.short_description = "Mark selected stories as published"

    fieldsets = (("Detail", {"fields": ("message", "approval")}),)


admin.site.register(Comment, CommentAdmin)
