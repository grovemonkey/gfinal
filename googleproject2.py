#! /usr/bin/env python3


import os
import sys
import requests

for files in os.listdir("/data/feedback/"):
    with open("/data/feedback/" + files) as file:
        a = file.read()
        b = a.split('\n')
        dictfile = {"title": b[0], "name": b[1], "date": b[2], "feedback": b[3]}
        requests.post("http://34.122.116.38/feedback/", data=dictfile)
        print(requests.status_code())
