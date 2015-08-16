from django.contrib.gis.geos import GEOSGeometry


METERS_PER_MILE = 1609.34

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
