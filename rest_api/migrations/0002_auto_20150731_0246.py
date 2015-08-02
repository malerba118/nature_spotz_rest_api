# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SmallIntegerField(null=True, choices=[(1, b'Running'), (2, b'Biking'), (3, b'Picnicking')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SmallIntegerField(null=True, choices=[(1, b'Waterfall'), (2, b'Pool'), (3, b'Overlook')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParkingLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('spot', models.ForeignKey(to='rest_api.Spot', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(null=True, upload_to=b'')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('spot', models.ForeignKey(to='rest_api.Spot', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.SmallIntegerField(null=True)),
                ('review', models.CharField(max_length=750, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('spot', models.ForeignKey(to='rest_api.Spot', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tip', models.CharField(max_length=750, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('spot', models.ForeignKey(to='rest_api.Spot', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='spot',
            name='activity_types',
            field=models.ManyToManyField(to='rest_api.ActivityType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spot',
            name='danger_level',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spot',
            name='description',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spot',
            name='family_safe',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spot',
            name='feature_types',
            field=models.ManyToManyField(to='rest_api.FeatureType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spot',
            name='skill_level',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spot',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spot',
            name='title',
            field=models.CharField(max_length=250, null=True),
            preserve_default=True,
        ),
    ]
