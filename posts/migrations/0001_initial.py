# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField(max_length=4000)),
                ('author', models.CharField(max_length=400, default='doe')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, unique=True, null=True)),
                ('publish', models.DateField(null=True, auto_now=True)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location, width_field='width_field', height_field='height_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created', '-date_updated'],
            },
        ),
    ]
