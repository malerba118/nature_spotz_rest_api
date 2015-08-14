from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
import django_filters
from rest_framework.filters import BaseFilterBackend
from rest_api.models import Spot, ActivityType, FeatureType, Favorite, Review
from rest_api.tools import parse_int, parse_float_list, get_curr_loc


class DistanceFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        radius = parse_int(request.query_params.get("radius", None))
        curr_loc = parse_float_list(request.query_params.get("curr_loc", None))

        if radius and len(curr_loc) == 2:
            return queryset.filter(location__distance_lte=(Point( curr_loc[0], curr_loc[1]), D(mi=radius)))
        return queryset

class SpotFilter(django_filters.FilterSet):

    title_contains = django_filters.CharFilter(name="title", lookup_type="icontains")
    min_skill = django_filters.NumberFilter(name="skill_level", lookup_type="gte")
    max_skill = django_filters.NumberFilter(name="skill_level", lookup_type="lte")
    min_danger = django_filters.NumberFilter(name="danger_level", lookup_type="gte")
    max_danger = django_filters.NumberFilter(name="danger_level", lookup_type="lte")
    activity_type = django_filters.MultipleChoiceFilter(name="activity_types", choices=ActivityType.types)
    feature_type = django_filters.MultipleChoiceFilter(name="feature_types", choices=FeatureType.types)
    family_safe = django_filters.BooleanFilter(name="family_safe")


    class Meta:
        model = Spot
        fields = ('family_safe', 'min_skill', 'max_skill', 'activity_type', 'feature_type')
        order_by = ["-created_at"]


class UserFavoriteFilter(django_filters.FilterSet):

    spot_id = django_filters.NumberFilter(name="spot__id", lookup_type="exact")

    class Meta:
        model = Favorite
        fields = ('spot_id',)

class UserReviewFilter(django_filters.FilterSet):

    spot_id = django_filters.NumberFilter(name="spot__id", lookup_type="exact")

    class Meta:
        model = Review
        fields = ('spot_id',)
