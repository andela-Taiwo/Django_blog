# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import csv
import io

def convert_header(csvHeader):
    header_ = csvHeader[0]
    cols = [x.replace(' ', '_').lower() for x in header_.split(",")]
    return cols


def stream_from_api(dir):
    reader = csv.reader(open(dir), dialect='excel')
    # reader = csv.reader(io_string, delimiter=';', quotechar='|')
    header_ = next(reader)
    header_cols = convert_header(header_)
    parsed_items = []

    '''
    if using a custom signal
    '''
    for line in reader:
        parsed_row_data = {}
        i = 0
        keys = []
        row_item = line[0].split('|')
        # import pdb;pdb.set_trace()
        key = header_cols[i]
        keys = key.split("|")
        parsed_row_data = dict(zip(keys, row_item))
        i += 1
        parsed_items.append(parsed_row_data)

    return parsed_items


def load_user(apps, schema_editor):
    User = apps.get_model('posts', 'USER')

    def stream_users():
        items = stream_from_api("posts/user_info.csv")
        for item in items:
            yield User(full_name=item['full_name'], email=item['email'],
                       password=item['password'],
                       date_created=item['date_created'])
    # Adjust (or remove) the batch size depending on your needs.
    # You won't be able to use this method if your objects depend on one-another
    User.objects.bulk_create(stream_users(), batch_size=100)


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20180204_0817'),
    ]
    # operations = [migrations.RunPython(load_user)]
    operations = [migrations.RunPython(load_user)]
