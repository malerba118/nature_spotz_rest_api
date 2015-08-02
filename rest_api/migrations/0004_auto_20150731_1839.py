# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_auto_20150731_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='danger_level',
            field=models.SmallIntegerField(null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='skill_level',
            field=models.SmallIntegerField(null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
            preserve_default=True,
        ),
    ]
