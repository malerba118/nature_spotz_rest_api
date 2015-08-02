# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_spot_primary_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='primary_image',
        ),
        migrations.AddField(
            model_name='spot',
            name='primary_photo',
            field=models.ImageField(null=True, upload_to=b'/images/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'/images/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='spot',
            field=models.ForeignKey(related_name='additional_photos', to='rest_api.Spot', null=True),
            preserve_default=True,
        ),
    ]
