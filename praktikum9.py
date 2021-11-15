# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:09:14 2021

@author:Novan Krisna
"""
print('program penjumlahan ')
def penjumlahan(angka = 0, jmlh=0 ,o=1):
    if (jmlh<=0):
        return 0
    else:
        angka = int(input('masukkan angka ke-'+str(o)+':'))
        if(jmlh==1):
            return angka
        
        else:
            o+=1
            return angka + penjumlahan (angka,jmlh-1,o)
        
jumlah = int(input('masukan jumlah:'))
nilai = penjumlahan(jmlh=jumlah)
print('hasil dari penjumlahan adalah:'+str(nilai))
            