# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(max_length=4000)),
                ('approval', models.CharField(max_length=2, default='DC', choices=[('AP', 'Approved'), ('DC', 'Declined')])),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, editable=False), size=None)),
                ('depth', models.PositiveSmallIntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default=1, to='posts.Post')),
            ],
            options={
                'ordering': ['-date_created', '-date_updated'],
            },
        ),
    ]
