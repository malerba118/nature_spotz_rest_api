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

def get_curr_loc(request):
    """
    Get GEOSGeometry Point from the request
    :param request:
    :return:
    """
    curr_loc_str = request.QUERY_PARAMS.get("curr_loc", None)
    curr_loc_lst = parse_float_list(curr_loc_str)

    if len(curr_loc_lst) == 2:
        curr_loc = GEOSGeometry("POINT(" + str(curr_loc_lst[0]) + " " + str(curr_loc_lst[1]) + ")")
        return curr_loc
    return None