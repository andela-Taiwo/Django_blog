# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=400)),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='user_id',
            field=models.ForeignKey(to='posts.User'),
        ),
    ]
