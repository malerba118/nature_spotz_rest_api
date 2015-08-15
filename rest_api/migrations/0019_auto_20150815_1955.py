# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0018_auto_20150815_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.SmallIntegerField(choices=[(1, b'Running'), (2, b'Biking'), (3, b'Picnicking')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='spot',
            field=models.ForeignKey(related_name='favorites', to='rest_api.Spot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(related_name='favorites', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featuretype',
            name='name',
            field=models.SmallIntegerField(choices=[(1, b'Waterfall'), (2, b'Pool'), (3, b'Overlook')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parkinglocation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parkinglocation',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parkinglocation',
            name='spot',
            field=models.ForeignKey(related_name='parking_locations', to='rest_api.Spot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to=b'additional-photos/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='spot',
            field=models.ForeignKey(related_name='additional_photos', to='rest_api.Spot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(related_name='reviews', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='spot',
            field=models.ForeignKey(related_name='reviews', to='rest_api.Spot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tip',
            name='author',
            field=models.ForeignKey(related_name='tips', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tip',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tip',
            name='spot',
            field=models.ForeignKey(related_name='tips', to='rest_api.Spot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tip',
            name='tip',
            field=models.CharField(max_length=750),
            preserve_default=True,
        ),
    ]
