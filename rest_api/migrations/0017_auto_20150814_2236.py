# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0016_auto_20150813_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='location',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=4326),
            preserve_default=True,
        ),
    ]
