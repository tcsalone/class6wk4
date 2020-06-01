#! /usr/bin/env python3

import os
import sys
from PIL import Image

srcDir = "/home/student-01-3376cba60dbf/supplier-data/images/"
destDir = "/home/student-01-3376cba60dbf/supplier-data/images/"
listOfFiles = list()


for (dirpath, dirnames, filenames) in os.walk(srcDir):
    listOfFiles += filenames

for infile in listOfFiles:
    fname, extension = os.path.splitext(infile)
    #print("f:", fname)
    #print("e: ",extension)
    outfile = destDir + fname + ".jpeg"
    infile = srcDir + fname + ".tiff"
    print(outfile)
    print("infile: ", infile)
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                print(im)
                rgb_im = im.convert("RGB")
                resize_im = rgb_im.resize((600, 400))
                resize_im.save(outfile, "JPEG") 
                print("Converstion complete: ", outfile)
        except IOError as err:
            print("I/O Error: {0}".format(err))
            print("Cannot convert", infile)
