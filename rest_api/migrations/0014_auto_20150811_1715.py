# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0013_auto_20150811_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkinglocation',
            name='spot',
            field=models.ForeignKey(related_name='parking_locations', to='rest_api.Spot', null=True),
            preserve_default=True,
        ),
    ]
