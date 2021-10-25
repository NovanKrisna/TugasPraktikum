# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:38:44 2021

@author: Asus X441U
"""

u = 0
t = 0
tampung = 0
while u != '':
 u = int(input('Masukkan umur: '))
 tampung += 1
 if (u == -1):
     break;
 elif 0 <= u <= 2:
     t += 0.0
     print('gratis')
     print('running total:',t)
 elif 3 <= u <= 12:
     t += 14.0
     print('harga $14.0')
     print('running total:',t)
     
 elif u >= 65:
     t+= 18.0
     print('harga $18.0')
     print('running total:',t)
 elif 13 <= u <= 64:
     t+= 23.0
     print('harga $23.0' )
     print('running total',t)


    



