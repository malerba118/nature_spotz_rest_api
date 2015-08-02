from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import GeoModelAdmin
from rest_api.models import Spot, Tip, ActivityType, Review, FeatureType, Photo, ParkingLocation

admin.site.register(Spot, GeoModelAdmin)
admin.site.register(Tip)
admin.site.register(ActivityType)
admin.site.register(FeatureType)
admin.site.register(Review)
admin.site.register(Photo)
admin.site.register(ParkingLocation)