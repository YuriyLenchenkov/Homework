#!/usr/bin/env python3

# import webbrowser
from geopy.geocoders import Nominatim

with open('/tmp/coord.txt', 'r') as f:
    coord = f.read().split(';')
longitude = coord[0].replace("'", "").replace(",", ".")
longitude10 = str(round((int(longitude.split(".")[1])/60 + int(longitude.split(".")[0])), 4))
#print(longitude10)
latitude = coord[1].replace("'", "").replace(",", ".")
latitude10 = str(round((int(latitude.split(".")[1])/60 + int(latitude.split(".")[0])), 4))
#print(latitude10)
url = "https://www.google.com/maps/search/?api=1&query=" + longitude10 + "," + latitude10
geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/92.0 Safari/537.36")
location_box = geolocator.reverse(longitude10 + "," + latitude10)
print(location_box.address)
print('Google maps URL: ', url)
# webbrowser.open_new(url)
