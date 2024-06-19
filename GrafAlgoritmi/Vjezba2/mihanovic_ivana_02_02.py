# -*- coding: utf-8 -*-
"""
Napisati program u kojem korisnik unosi granice dvaju zatvorenih intervala 
[a, b] i [c, d] i ispisuje njihov presjek. Primjer: Za intervale [1, 5]
i [-3, 2], presjek je interval [1, 2], a za intervale [-3.5, 2] i [4, 6.5]
presjek je prazan skup.
"""
lst1=[]
lst2=[]

print("Prve granice")
x=float(input())
y=float(input())
lst1.append(x)
lst1.append(y)

print("Druge granice")
k=float(input())
z=float(input())
lst2.append(k)
lst2.append(z)

lst1.sort()
print(lst1)
lst2.sort()
print(lst2)

lst=[]
if(lst2[0]<lst1[1] and lst2[1]>=lst1[0]):
    if(lst1[0]<lst2[0]):
        lst.append(lst2[0])
    else:
        lst.append(lst1[0])
    if(lst1[1]<lst2[1]):
        lst.append(lst1[1])
    else:
        lst.append(lst2[1])       
print(lst)