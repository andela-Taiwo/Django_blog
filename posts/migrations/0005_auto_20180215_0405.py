# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180215_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height_field',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='width_field',
            field=models.IntegerField(null=True, default=0),
        ),
    ]
