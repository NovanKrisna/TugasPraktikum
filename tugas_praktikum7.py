# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:14:04 2021

@author: Novan Krisna
NIM:065002100030
Praktikum
"""

print("menghitung tanggal tiap bulan")

def days (n=0, o=0):
    n=True
    while n:
        n=int(input("masukan bulan [1-12]: "))
        if n>=13 or n<=-1:
            print("error") 
            print("tekan 0 untuk end the program")
        elif n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
            print("ada 31 hari dalam satu bulan")
            print("tekan 0 untuk end the program")
        elif n==4 or n==6 or n==9 or n==11:
            print("ada 30 hari dalam satu bulan")
            print("tekan 0 untuk end the program")
        elif n==2:
            o=int(input("masukan tahun: "))
            if(o%4==0 and o==2):
               print("ada 29 hari dalam satu bulan")
               print("tekan 0 untuk end the program")
            else:
                print("ada 28 hari dalam satu bulan")
                print("tekan 0 untuk end the program")
            
        if n==0:
            return n
            
month_year = days()
print("program berakhir")
print("terimakasih dan sampaijumpa")