# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0021_auto_20150815_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuretype',
            name='name',
            field=models.SmallIntegerField(choices=[(0, b'Beach'), (5, b'Hot Spring'), (10, b'Lake'), (15, b'Mountain'), (20, b'Overlook'), (25, b'Pond'), (30, b'Pool'), (35, b'River'), (40, b'Stream'), (45, b'Trail'), (50, b'Waterfall'), (18, b'Other')]),
            preserve_default=True,
        ),
    ]
