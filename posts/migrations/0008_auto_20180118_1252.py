# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20180118_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
