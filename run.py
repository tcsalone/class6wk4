#! /usr/bin/env python3

import os
import requests

srcDir = "/home/student-03-b3dd264fea1d/supplier-data/descriptions/"

for (dirname, dirpath, filename) in os.walk(srcDir):
    for file in filename:
        print(os.path.join(dirname, file))
        with  open(os.path.join(dirname, file), 'r') as opened:
            for line in opened:
                print(line)
