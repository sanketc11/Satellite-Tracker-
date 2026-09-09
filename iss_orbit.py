from vpython import *
from skyfield.api import load
import requests
import math

EARTH_RADIUS = 6.371

stations_url = "https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=tle"

satellites = load.tle_file(stations_url)
iss = satellites[0]

ts = load.timescale()

print("Tracking:", iss.name)


earth = sphere(
    pos=vector(0, 0, 0),
    radius=EARTH_RADIUS,
    texture=textures.earth
)


satellite = sphere(
    pos=vector(0, 0, 0),
    radius=0.15,
    color=color.red,
    make_trail=True,
    trail_radius=0.025
)

satellite_label = label(
    pos=satellite.pos,
    text=" ISS",
    xoffset=10,
    yoffset=10,
    height=15,
    box=False,
    opacity=0
)

title = label(
    pos=vector(-10, 7, 0),
    text="ISS SATELLITE TRACKER",
    height=25,
    box=False
)

info = label(
    pos=vector(-10, 5, 0),
    text="Loading...",
    height=16,
    box=False
)


def get_position(t):

    geocentric = iss.at(t)

    x, y, z = geocentric.position.km

    scale = EARTH_RADIUS / 6371

    return vector(
        x * scale,
        y * scale,
        z * scale
    )

now = ts.now()

orbit_points = []

for minutes in range(0, 91, 2):

    t = ts.tt_jd(
        now.tt + minutes / (24 * 60)
    )

    orbit_points.append(
        get_position(t)
    )

orbit = curve(
    pos=orbit_points,
    color=color.yellow,
    radius=0.025
)

api_url = "https://api.wheretheiss.at/v1/satellites/25544"

while True:

    try:

       
        response = requests.get(api_url,timeout=7)

        data = response.json()

        latitude = float(data["latitude"])
        longitude = float(data["longitude"])
        altitude = float(data["altitude"])
        velocity = float(data["velocity"])

        t = ts.now()

        satellite.pos = get_position(t)

        # Move label with satellite
        satellite_label.pos = satellite.pos


        info.text = (
            f"Latitude:   {latitude:.2f}°\n"
            f"Longitude:  {longitude:.2f}°\n"
            f"Altitude:   {altitude:.2f} km\n"
            f"Velocity:   {velocity:.2f} km/h"
        )

        earth.rotate(
            angle=0.002,
            axis=vector(0, 1, 0)
        )

        rate(30)

    except Exception as e:

        print("Error:", e)

        rate(1)