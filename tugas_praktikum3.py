# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:15:39 2021

@author: Asus X441U
"""
import math 
a = float(input("Masukkan nilai A: "))
b = float(input("Masukkan nilai B: "))
c = float(input("masukkan nilai C: "))

d = (b**2) - (4*a*c)



if (a == 0):
    print('bukan termasuk persamaan kuadrat')
elif (d == 0):
    x1 = (-b/(2*a))
    print("persamaan kuadrat:",a ,"x^2",+ b,"x",+c)
    print("determinannya adalah",d)
    print("akar:",x1)
elif (d < 0 ):
    print("persamaan kuadrat:",a ,"x^2",+ b,"x",+c)
    print("determinannya adalah",d)
    print(-b,"+akar",d,"/2*",a )
    print(-b,"-akar",d,"/2*",a )
elif (d > 0 ):
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print("persamaan kuadrat:",a ,"x^2",+ b,"x",+c)
    print("determinannya adalah",d)
    print("akar x1:",x1)
    print('akar x2:',x2)

    