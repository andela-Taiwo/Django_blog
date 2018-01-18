# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20171218_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.TextField(max_length=400, default='doe'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=400),
        ),
    ]
