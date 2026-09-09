from skyfield.api import EarthSatellite, load
import requests

# 1. Fetch current TLE for ISS from Celestrak
url = "https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE"
response = requests.get(url)
lines = response.text.strip().splitlines()

line1 = lines[1]
line2 = lines[2]

# 2. Load timescale and build the satellite object
ts = load.timescale()
satellite = EarthSatellite(line1, line2, "ISS", ts)

# 3. Propagate to current time
t = ts.now()
geocentric = satellite.at(t)

# 4. Get position/velocity (x,y,z / vx,vy,vz) — matches your diagram
position = geocentric.position.km      # (x, y, z) in km
velocity = geocentric.velocity.km_per_s  # (vx, vy, vz) in km/s

# 5. Convert to lat/lon/altitude
subpoint = geocentric.subpoint()
lat = subpoint.latitude.degrees
lon = subpoint.longitude.degrees
alt_km = subpoint.elevation.km

# 6. Speed for your "speed display" branch
import numpy as np
speed_km_s = np.linalg.norm(velocity)

print(f"Lat: {lat:.2f}, Lon: {lon:.2f}, Alt: {alt_km:.2f} km")
print(f"Speed: {speed_km_s:.2f} km/s")