# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20171217_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=40, unique=True)),
                ('content', models.CharField(max_length=400)),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
                ('user_id', models.ForeignKey(to='posts.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
