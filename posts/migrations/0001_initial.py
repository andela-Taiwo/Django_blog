# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=32, default='John')),
                ('last_name', models.CharField(max_length=32, default='Doe')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location, width_field='width_field', height_field='height_field')),
                ('height_field', models.IntegerField(null=True, default=0)),
                ('width_field', models.IntegerField(null=True, default=0)),
                ('gender', models.CharField(max_length=10, blank=True, null=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
