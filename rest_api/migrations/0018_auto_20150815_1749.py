# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0017_auto_20150814_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='primary_photo',
            field=models.FileField(upload_to=b'primary-photos/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='title',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='user',
            field=models.ForeignKey(related_name='spots', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
