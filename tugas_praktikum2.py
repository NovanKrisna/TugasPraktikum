# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 09:21:26 2021

@author: Novan Krisna
NIM:065002100030
"""
import math
lat1= eval(input("masukan latitude kota pertama:"))
lon1= eval(input("masukan longitude kota pertama:"))
lat2= eval(input("masukan latitude kota kedua:"))
lon2= eval(input("masukan longitude kota kedua:"))


radius = 6371
dlat = math.radians(lat2-lat1)
dlon = math.radians(lon2-lon1)
a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin (dlon/2)**2 
c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
d = radius * c
   
print("jadi jarak anatar kedua kota :",d,"kilometer")   