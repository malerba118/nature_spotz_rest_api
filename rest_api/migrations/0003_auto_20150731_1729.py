# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20150731_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='location',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=4326, null=True),
            preserve_default=True,
        ),
    ]
