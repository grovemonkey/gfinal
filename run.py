#! /usr/bin/env python3

import os
import requests

url = "http://adress/directory/"
filedirectory = '/supplier-data/descriptions/'
filelist = os.listdir(filedirectory)
for file in filelist:
    if file.endswith("txt"):
        fileopen = open(filedirectory + file)
        imgname = os.path.splitext(file)[0]
        infor = fileopen.read().replace("lbs", "").split('\n')
        dic = {"name": infor[0], "weight": int(infor[1]), "description": info[2], "image_name": imgname + ".jpeg"}
        response = requests.post(url, json=dic)
        response.raise_for_status()
        print(response.status_code)
