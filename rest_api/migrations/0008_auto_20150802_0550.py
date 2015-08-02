# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0007_auto_20150801_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='primary_photo',
            field=models.FileField(null=True, upload_to=b'/images/'),
            preserve_default=True,
        ),
    ]
