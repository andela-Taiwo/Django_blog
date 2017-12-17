# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateField(default=datetime.date.today, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='date_updated',
            field=models.DateField(default=datetime.date.today, auto_now=True),
            preserve_default=False,
        ),
    ]
