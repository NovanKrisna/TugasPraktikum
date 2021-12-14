# -*- coding: utf-8 -*-
"""
Created on Tue Dec 07 08:18:45 2021

@author: Novan Krisna

"""

def menukar(A, i, k):
    temp = A[i]
    A[i] = A[k]
    A[k] = temp

def bubbleSort(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            menukar(A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)

A = [3, 5, 8, 4, 1, 9, -2]
bubbleSort(A, len(A))
print("List yang sudah disorting")
print(A)