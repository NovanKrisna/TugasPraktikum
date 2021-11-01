# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:18:44 2021

@author: Novan Krisna
NIM:065002100030
"""
def kateg(n="0",total=0,menampung=0 ):
    while (n != "") :
        n = str(input("masukkan nilai :"))
        menampung = menampung + 1
        if (n == ''):
            return total/(menampung -1)
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
        elif (n== "C"):
            print('nilai=1.75')
            total += 1.75
        elif (n== "D"):
            print('nilai=1.5')
            total += 1.5
        else :
            print ("masukan nilai valid ya")
            
rata_rata = kateg ()
print("rata-ratanya adalah",rata_rata)
