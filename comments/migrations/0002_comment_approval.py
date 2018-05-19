# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approval',
            field=models.CharField(max_length=2, default='DC', choices=[('AP', 'Approved'), ('DC', 'Declined')]),
        ),
    ]
