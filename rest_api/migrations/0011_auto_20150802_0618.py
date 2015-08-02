# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0010_auto_20150802_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'additional-photos/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='primary_photo',
            field=models.FileField(null=True, upload_to=b'primary-photos/'),
            preserve_default=True,
        ),
    ]
