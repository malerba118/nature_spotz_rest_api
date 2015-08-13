from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from django.db import models
from django.contrib.gis.db.models import PointField, LineStringField, GeoManager


# Create your models here.


class FeatureType(models.Model):
    WATERFALL = 1
    POOL = 2
    OVERLOOK = 3
    types = (
        (WATERFALL, "Waterfall"),
        (POOL, "Pool"),
        (OVERLOOK, "Overlook"),
    )
    name = models.SmallIntegerField(choices=types, null=True)

    def __unicode__(self):
        return dict(self.types)[self.name]

class ActivityType(models.Model):
    RUNNING = 1
    BIKING = 2
    PICNICKING = 3
    types = (
        (RUNNING, "Running"),
        (BIKING, "Biking"),
        (PICNICKING, "Picnicking"),
    )
    name = models.SmallIntegerField(choices=types, null=True)

    def __unicode__(self):
        return dict(self.types)[self.name]


class Spot(models.Model):
    DANGER_LEVEL_CHOICES = [(i,i) for i in range(1, 11)]
    SKILL_LEVEL_CHOICES = [(i,i) for i in range(1, 11)]

    user = models.ForeignKey(User, related_name="spots", null=True)
    primary_photo = models.FileField(upload_to="primary-photos/", null=True)
    title = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=1000, null=True)
    skill_level = models.SmallIntegerField(choices=SKILL_LEVEL_CHOICES, null=True)
    danger_level = models.SmallIntegerField(choices=DANGER_LEVEL_CHOICES, null=True)
    family_safe = models.NullBooleanField(null=True)
    location = LineStringField(null=True)
    feature_types = models.ManyToManyField(FeatureType, null=True)
    activity_types = models.ManyToManyField(ActivityType, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    objects = GeoManager()

    def __unicode__(self):
        return self.title

    def getRouteLength(self):
        return self.location.length





class ParkingLocation(models.Model):
    spot = models.ForeignKey(Spot, related_name="parking_locations", null=True)
    location = PointField(null=True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    objects = GeoManager()


class Photo(models.Model):
    spot = models.ForeignKey(Spot, related_name="additional_photos", null=True)
    photo = models.ImageField(upload_to="additional-photos/", null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)


class Review(models.Model):
    RATING_CHOICES = [(i,i) for i in range(1, 6)]
    spot = models.ForeignKey(Spot, related_name="reviews", null=True)
    author = models.ForeignKey(User, related_name="reviews", null=True)
    rating = models.SmallIntegerField(choices=RATING_CHOICES, null=True)
    review = models.CharField(max_length=750, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

class Tip(models.Model):
    spot = models.ForeignKey(Spot, related_name="tips", null=True)
    author = models.ForeignKey(User, related_name="tips", null=True)
    tip = models.CharField(max_length=750, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="favorites", null=True)
    spot = models.ForeignKey(Spot, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)