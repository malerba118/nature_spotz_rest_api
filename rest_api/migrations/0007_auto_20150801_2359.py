# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0006_auto_20150801_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(related_name='reviews', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tip',
            name='author',
            field=models.ForeignKey(related_name='tips', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.SmallIntegerField(null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='spot',
            field=models.ForeignKey(related_name='reviews', to='rest_api.Spot', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tip',
            name='spot',
            field=models.ForeignKey(related_name='tips', to='rest_api.Spot', null=True),
            preserve_default=True,
        ),
    ]
