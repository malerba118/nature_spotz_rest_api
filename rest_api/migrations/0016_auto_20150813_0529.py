# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0015_auto_20150811_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='spot',
            field=models.ForeignKey(related_name='favorites', to='rest_api.Spot', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='activity_types',
            field=models.ManyToManyField(related_name='spots', null=True, to='rest_api.ActivityType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='feature_types',
            field=models.ManyToManyField(related_name='spots', null=True, to='rest_api.FeatureType'),
            preserve_default=True,
        ),
    ]
