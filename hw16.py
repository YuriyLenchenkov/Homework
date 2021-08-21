#!/usr/bin/env python3

from geopy.geocoders import Nominatim

with open('/tmp/coord.txt', 'r') as f:
    coord = f.read().split(';')
    print(coord[0], coord[1])
longitude = coord[0].replace("'", "").replace(",", ".")
print(longitude)
longitude10 = str( round(int(longitude.split(".")[1])/60 + int(longitude.split(".")[0]), 5))

latitude = coord[1].replace("'", "").replace(",", ".")

latitude10 = str(round((int(latitude.split(".")[1])/60 + int(latitude.split(".")[0])), 5))
if float(latitude) < 0:
    latitude10 = str(float(latitude10) * -1)
if float(longitude) < 0:
    latitude10 = str(float(latitude10) * -1)

url = "https://www.google.com/maps/search/?api=1&query=" + longitude10 + "," + latitude10
geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/92.0 Safari/537.36")
location_box = geolocator.reverse(longitude10 + "," + latitude10)
print(location_box.address)
print('Google maps URL: ', url)

