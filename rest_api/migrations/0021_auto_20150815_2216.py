# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0020_auto_20150815_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.SmallIntegerField(choices=[(0, b'Biking'), (5, b'Birding'), (10, b'Bouldering'), (15, b'Camping'), (20, b'Day-tripping'), (25, b'Fishing'), (30, b'Hiking'), (35, b'Kayaking'), (40, b'Picnicking'), (45, b'Running'), (50, b'Spelunking'), (55, b'Swimming'), (38, b'Other')]),
            preserve_default=True,
        ),
    ]
