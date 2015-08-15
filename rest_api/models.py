from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db.models import PointField, LineStringField, GeoManager


# Create your models here.
from django.utils import timezone


class FeatureType(models.Model):
    WATERFALL = 1
    POOL = 2
    OVERLOOK = 3
    types = (
        (WATERFALL, "Waterfall"),
        (POOL, "Pool"),
        (OVERLOOK, "Overlook"),
    )
    name = models.SmallIntegerField(choices=types)

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
    name = models.SmallIntegerField(choices=types)

    def __unicode__(self):
        return dict(self.types)[self.name]


class Spot(models.Model):
    DANGER_LEVEL_CHOICES = [(i,i) for i in range(1, 11)]
    SKILL_LEVEL_CHOICES = [(i,i) for i in range(1, 11)]

    user = models.ForeignKey(User, related_name="spots")
    primary_photo = models.FileField(upload_to="primary-photos/")
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, null=True)
    skill_level = models.SmallIntegerField(choices=SKILL_LEVEL_CHOICES, null=True)
    danger_level = models.SmallIntegerField(choices=DANGER_LEVEL_CHOICES, null=True)
    family_safe = models.NullBooleanField(null=True)
    location = LineStringField()
    feature_types = models.ManyToManyField(FeatureType, related_name="spots", null=True)
    activity_types = models.ManyToManyField(ActivityType, related_name="spots", null=True)
    created_at = models.DateTimeField(default=timezone.now)
    objects = GeoManager()

    def __unicode__(self):
        return self.title





class ParkingLocation(models.Model):
    spot = models.ForeignKey(Spot, related_name="parking_locations")
    location = PointField()
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    objects = GeoManager()


class Photo(models.Model):
    spot = models.ForeignKey(Spot, related_name="additional_photos")
    photo = models.ImageField(upload_to="additional-photos/")
    created_at = models.DateTimeField(default=timezone.now)


class Review(models.Model):
    RATING_CHOICES = [(i,i) for i in range(1, 6)]
    spot = models.ForeignKey(Spot, related_name="reviews")
    author = models.ForeignKey(User, related_name="reviews")
    rating = models.SmallIntegerField(choices=RATING_CHOICES)
    review = models.CharField(max_length=750, null=True)
    created_at = models.DateTimeField(default=timezone.now)

class Tip(models.Model):
    spot = models.ForeignKey(Spot, related_name="tips")
    author = models.ForeignKey(User, related_name="tips")
    tip = models.CharField(max_length=750)
    created_at = models.DateTimeField(default=timezone.now)


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="favorites")
    spot = models.ForeignKey(Spot, related_name="favorites")
    created_at = models.DateTimeField(default=timezone.now)