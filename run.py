#! /usr/bin/env python3

import os
import requests

srcDir = "/home/student-01-c4b067d66a1f/supplier-data/descriptions/"

for (dirname, dirpath, filename) in os.walk(srcDir):
    for file in filename:
        #print(file)
        temp={}
        name = ['name', 'weight', 'description']
        with  open(os.path.join(dirname, file), 'r') as opened:
            lines = opened.readlines()
        for i in range(len(name)):
            temp[name[i]]=lines[i].rstrip("\n")
        
        img_name = file.replace('txt', 'jpeg')
        temp['image_name']=img_name
       
        weight_conv=temp.get("weight")
        temp['weight']=(int(weight_conv.replace('lbs', '')))
        
        print(temp)
        response = requests.post("http://35.239.95.68/fruits/", json=temp)
        
