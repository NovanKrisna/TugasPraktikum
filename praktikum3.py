# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:15:16 2021

@author: Novan Krisna
NIM : 065002100030
"""
a = float(input("Masukkan panjang sisi A: "))
b = float(input("Masukkan panjang sisi B: "))
c = float(input("masukkan panjang sisi C: "))

if (a == b == c):
    print("ini merupakan segitiga sama sisi")
elif (a + b <= c) or (a + c <=b ) or (b + c <=a):
    print("ini bukan merupakan segita")
elif ( a == b or b == c or c == a):
    print("ini merupakan segitiga sama kaki")
    
else:
    print("ini merupakan segituga sembarang ")
