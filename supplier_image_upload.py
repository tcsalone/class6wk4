#! /usr/bin/env python3

import requests
import sys
import os

listOfFiles = []
srcDir = "/home/student-01-c4b067d66a1f/supplier-data/images/"
url = "http://localhost/upload/"

for (dirpath, dirname, filename) in os.walk(srcDir):
    for file in filename:
        if file.endswith(".jpeg"):
            print(file)
            listOfFiles.append(file)

for each in listOfFiles:
    upload=(srcDir+each)
    with open(upload, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

