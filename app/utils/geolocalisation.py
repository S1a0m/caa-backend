from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def find_nearest_point(target, points):
    min_distance = float('inf')
    nearest = None
    for point in points:
        dist = haversine(target[0], target[1], point[0], point[1])
        if dist < min_distance:
            min_distance = dist
            nearest = point
    return nearest
