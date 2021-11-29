# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:50:35 2021

@author: Asus X441U
"""
def bubble_sort(a):
	n = len(a)
	for i in range(n):
		for j in range(0, n-i-1):
			if a[j] > a[j+1] :
				a[j], a[j+1] = a[j+1], a[j]

print('Sebelum disorting: [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]')
angka = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
bubble_sort(angka)

def binary_search(angka, num_find):
    start = 0
    end = len(angka) - 1
    mid = (start + end)//2
    found = False
    position = -1
    while start <= end:
        if angka[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > angka[mid]:
            start = mid + 1
            mid = (start + end)//2
        else:
            end = mid - 1
            mid = (start + end)//2
            
    print("Sesudah di Sorting: ", angka)
    return (found, position-1)

num = int(input('Masukkan angka yang dicari: '))
found = binary_search(angka, num)
if found[0]:
    print('Nomor %d ditemukan di posisi %d'%(num, found[1]+2))
else:
    print('Nomor %d tidak ditemukan'%num)