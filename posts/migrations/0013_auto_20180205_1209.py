# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models, migrations
from django.utils.text import slugify
import django.core.validators


def slugify_title(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    Post = apps.get_model('posts', 'Post')
    for post in Post.objects.all():
        post.slug = slugify(post.title)
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20180205_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='Post',
            name='slug',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(re.compile('^[0-9a-z-]+$'), 'Enter a valid slug.', 'invalid')], help_text='Required. 2 to 30 characters and can only contain a-z, 0-9, and the dash (-)', unique=False, db_index=False, null=True),
            preserve_default=False,
        ),
        migrations.RunPython(slugify_title),
        migrations.AlterField(
            model_name='Post',
            name='slug',
            field=models.CharField(help_text='Required. 2 to 30 characters and can only contain a-z, 0-9, and the dash (-)', unique=True, max_length=100, db_index=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(re.compile('^[0-9a-z-]+$'), 'Enter a valid slug.', 'invalid')]),
        ),
    ]
