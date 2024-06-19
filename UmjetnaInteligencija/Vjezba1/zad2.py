# -*- coding: utf-8 -*-
"""
2.	Funkcije koja će za listu 2D koordinata (parovi brojeva) koja predstavlja 
vrhove poligona:
a.	izračunati opseg poligona
b.	Izračunati središte poligona
c.	Izračunati minimalan radijus kruga koji opisuje poligon

"""
import math

def opsegPoligona(lst):
    opseg = 0
    for i in range(len(lst)-1):
        opseg += math.dist(lst[i],lst[i+1])
    opseg += math.dist(lst[-1],lst[0])
    return opseg

def sredistePoligona(lst):
    sumOfX = sum(x for x, _ in lst)
    sumOfY = sum(y for _, y in lst)
    return sumOfX/len(lst),sumOfY/len(lst)

def minimalanRadijusKruga(lst, sredistePoligona):
    return max([math.dist(el, sredistePoligona) for el in lst])

lst = [(1,3),(2,1),(3,5),(0,2),(1,2)]
print(opsegPoligona(lst))

sredistePoligona = sredistePoligona(lst)
print(sredistePoligona)
print(minimalanRadijusKruga(lst, sredistePoligona))