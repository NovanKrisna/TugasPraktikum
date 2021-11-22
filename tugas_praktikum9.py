# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:01:24 2021

@author: Novan Krisna
"""

print('Ini Merupakan Program Pemangkatan Negatif Dan Positif')

def positif(x) :
       i = int(input('Masukkan Pangkatnya :'))
       pangkat = x ** i
       print('Hasilnya Adalah', pangkat) 

def negatif(x) : 
       i = int(input('Masukkan Pangkatnya :')) 
       pangkat = x ** i
       print('Hasilnya Adalah', pangkat) 
x = int(input('Masukkan Angka :')) 
if x >= 0 :
    positif(x) 
elif x <= 0 :
    negatif(x) 
else :
    print('Tolong Masukkan Angka')