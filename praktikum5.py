# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 07:21:19 2021

@author: Asus X441U
"""
n = '0'
total = 0
menampung = 0

while (n != "") :
    n = str(input("masukkan nilai :"))
    menampung = menampung + 1
    if (n == ''):
        break ;
    elif (n== 'A'):
        print ("nilai = 4.00")
        total += 4.00
    elif (n == 'A-'):
        print ("nilai = 3.75")
        total += 3.75
    elif (n== 'B+'):
        print ("nilai = 3.50")
        total += 3.50
    elif (n == 'B'):
        print ("nilai = 3.00")
        total += 3.00
    elif (n== 'B-'):
        print ("nilai = 2.75")
        total += 2.75
    else :
        menampung = menampung-1
        print ("masukkan nilai yang benar")
if (menampung ==1):
        print ("rata ratanya adalah 0")
else :
        avrg  = total/(menampung-1)
        print ("rata ratanya adalah :", avrg)
    
    