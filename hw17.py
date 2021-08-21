#!/usr/bin/env python3
from exif import Image

with open("/tmp/london-bridge.jpg", 'rb') as file:
    img = Image(file)
latitude = img.gps_latitude
longitude = img.gps_longitude

# print(img.gps_latitude, img.gps_latitude_ref, img.gps_longitude, img.gps_longitude_ref)

latitude_exp = str(int(latitude[0])) + "," + str(int(latitude[1])).replace(".","") + "'"
longitude_exp = str(int(longitude[0])) + "," + str(int(longitude[1])).replace(".","") + "'"

if img.gps_latitude_ref == "S":
    latitude_exp = "-" + latitude_exp
if img.gps_longitude_ref == "W":
    longitude_exp = "-" + longitude_exp

coord_exp = latitude_exp + ";" + longitude_exp
with open("/tmp/coord.txt", "w") as file:
    file.write(coord_exp)
