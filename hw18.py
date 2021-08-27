#!/usr/bin/env python3

import os
import sys
from PIL import Image

# script arg sets image max target size in bytes
arg = sys.argv[1]
# arg = 200000
file = "/tmp/london-bridge.jpg"
file_res = "/tmp/london-bridge_resize.jpg"

with Image.open(file) as img:
    img.load()
    width, height = img.size
ratio = width/height

img_resize = img.resize((height, width), Image.ANTIALIAS)
img.close()
img_resize.save(file_res, format='JPEG')
img_resize.close()

while os.path.getsize(file_res) >= int(arg):
    img_resize = Image.open(file_res)
    img_resize = img_resize.resize((int(width), int(height)))
    img_resize.save(file_res, format='JPEG')
    img.close()
    width = width * 0.9
    height = height * 0.9
