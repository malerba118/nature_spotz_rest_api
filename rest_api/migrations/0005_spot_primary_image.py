# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20150731_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='primary_image',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
