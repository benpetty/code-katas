"""Python Practice: Distance Between Points.

Below is a function that will calculate the shortest distance
between any two points on the Earth’s surface.
Do not worry about how it works.
It is simply a tool for this exercise.:

------- calculate_distance(point1, point2) ---------------------------------- #

The JSON file at this URL (contains some cities with international airports,
each with a latitude, a longitude, and a city that it connects to.
For the curious, the list of airports comes from Wikipedia.

Write a function that,

- given a starting city and an ending city,
will return a path between the two cities (including the two cities).
- also returns the total distance traveled between cities.
- appropriately handles the situation where no path exists.

Stretch Goals---------------------------------------------------------------- #
Try to incorporate any (or all) of these.
They are/can be independent of each other.

- Add to your function a parameter that makes it return
the shortest path (lowest distance) between the two cities.
- Add to your function a parameter that makes it return
the path with the fewest stops between the two cities.
- Have your function take a parameter for
a limit to the distance between any two cities.
- If specified, your function returns a path where each city-to-city jump
is less than or equal to that limit.
"""


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.

    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = (math.sin(0.5 * delta_phi)**2 +
         math.cos(phi1) *
         math.cos(phi2) *
         math.sin(0.5 * delta_lam)**2
         )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles
