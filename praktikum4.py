# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:20:37 2021

@author: Novan Krisna
NIM:065002100030
"""

h=int(input('mau berapa angka:'))

for i in range(0, h):
    for j in range(h, 0, - 1):
        print(h , end='')
    h -= 1
    print()