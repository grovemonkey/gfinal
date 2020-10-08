#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module
directory = os.listdir("supplier-data/images/")
url = "http://localhost/upload/"
for jpgfile in directory:
	if jpgfile.endswith(".jpeg"):
		with open("supplier-data/images/" + jpgfile, 'rb') as opened:
			r = requests.post(url, files={'file': opened})
