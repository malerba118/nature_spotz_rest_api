from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db.models import PointField, LineStringField, GeoManager


# Create your models here.
from django.utils import timezone


class FeatureType(models.Model):
    BEACH = 0
    HOT_SPRING = 5
    LAKE = 10
    MOUNTAIN = 15
    OTHER = 18
    OVERLOOK = 20
    POND = 25
    POOL = 30
    RIVER = 35
    STREAM = 40
    TRAIL = 45
    WATERFALL = 50

    types = (
        (BEACH, "Beach"),
        (HOT_SPRING, "Hot Spring"),
        (LAKE, "Lake"),
        (MOUNTAIN, "Mountain"),
        (OVERLOOK, "Overlook"),
        (POND, "Pond"),
        (POOL, "Pool"),
        (RIVER, "River"),
        (STREAM, "Stream"),
        (TRAIL, "Trail"),
        (WATERFALL, "Waterfall"),
        (OTHER, "Other"),
    )
    name = models.SmallIntegerField(choices=types)

    def __unicode__(self):
        return dict(self.types)[self.name]

class ActivityType(models.Model):
    #Incremented by 5's to allow insertion of new types in the future while retaining alphabetical order
    BIKING = 0
    BIRDING = 5
    BOULDERING = 10
    CAMPING = 15
    DAY_TRIPPING = 20
    FISHING = 25
    HIKING = 30
    KAYAKING = 35
    OTHER = 38
    PICNICKING = 40
    RUNNING = 45
    SPELUNKING = 50
    SWIMMING = 55


    types = (
        (BIKING, "Biking"),
        (BIRDING, "Birding"),
        (BOULDERING, "Bouldering"),
        (CAMPING, "Camping"),
        (DAY_TRIPPING, "Day-tripping"),
        (FISHING, "Fishing"),
        (HIKING, "Hiking"),
        (KAYAKING, "Kayaking"),
        (PICNICKING, "Picnicking"),
        (RUNNING, "Running"),
        (SPELUNKING, "Spelunking"),
        (SWIMMING, "Swimming"),
        (OTHER, "Other"),
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