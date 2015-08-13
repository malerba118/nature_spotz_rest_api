# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0014_auto_20150811_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='user',
            field=models.ForeignKey(related_name='spots', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
