# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:59:44 2021

@author: novan krisna
nim:065002100030
"""

n = input("masukkan namamu:")
o = input("masukkan nim kamu:")
p = input("masukkan tahun angkatanmu:")


class mhs:
    mCount = 0
    
    def __init__(self, nama_mhs, nim_mhs, angkatan_mhs):
        self.nama_mhs = nama_mhs
        self.nim_mhs = nim_mhs
        self.angkatan_mhs = angkatan_mhs
        mhs.mCount += 1
        
    def printy(self):
        print("Nama: " + self.nama_mhs + "\nNim: " + str(self.nim_mhs) + "\nAngkatan:" + str(self.angkatan_mhs)) 
                
mahasiswa = mhs(n, o, p)
mahasiswa.printy()




print("Jumlah Mahasiswa yang dimasukkan ke dalam objek adalah: ", mhs.mCount)
