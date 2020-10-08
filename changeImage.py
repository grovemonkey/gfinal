
from PIL import Image
import os
import sys

location = "supplier-data/images/"
for subdir, dirs, files in os.walk(location):
    for filename in files:
        if filename.endswith(".tiff"):
            front = os.path.splitext(filename)[0]
            outfile = location + front + ".jpeg"
            Image.open(location + filename).resize((600, 400)).convert('RGB').save(outfile, "JPEG")
