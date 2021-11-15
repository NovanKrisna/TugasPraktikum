# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 00:42:52 2021

@author: Novan Krisna
"""

f = False

def satu():
    print("(", x,  "'st')")
def dua():
    print("(", x, "'nd')")
def tiga():
    print("(", x, "'rd')")
def seterusnya():
    print("(", x, "'th')")


while (not f) :
    
    x = int(input("Masukkan Angka :"))
    
    if (x == 0):
        f = True
        print('0 th')
        print('makasih udah menggunakan programku')
    elif x == 1:
        satu()
    elif x == 2:
        dua()
    elif x == 3:
        tiga()
    elif x >= 4:
        seterusnya()
    else :
        print('Masukkan Angka Yang Benar ')