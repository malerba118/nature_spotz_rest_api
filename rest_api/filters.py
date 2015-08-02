from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework.filters import BaseFilterBackend


class DistanceFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        radius = parse_int(request.query_params.get("radius", None))
        curr_loc = parse_float_list(request.query_params.get("currLoc", None))

        if radius and len(curr_loc) == 2:
            return queryset.filter(location__distance_lte=(Point( curr_loc[0], curr_loc[1]), D(mi=radius)))
        return queryset


def parse_int(s):
    if is_number(s):
        return int(float(s))
    return None

def parse_float_list(lst):
    if lst:
        lst = lst.split(",")
        return [float(s) for s in lst if is_number(s)]
    return[]

def is_number(s):
    if (s):
        return s.replace(".", "").replace("-", "").isnumeric()
    return False

