# -*- coding: utf-8 -*-
"""
Napisati program u kojem se unose trojke brojeva. Za svaku trojku ispitati 
da li je pitagorejska trojka (brojevi zadovoljavaju pitagorin teorem).
Unos ponavljati sve dok se ne unese barem jedan negativni broj ili nula
"""

print("Enter numbers:")
x = int(input())
y = int(input())
z = int(input())
lst = []
while(x>0 and y>0 and z>0):
    lst.append(x)
    lst.append(y)
    lst.append(z)
    lst.sort()
    if(lst[2]**2==lst[1]**2 + lst[0]**2):
        print("Pitagorejska trojka: ",x,y,z)
    else:
        print("Nije pitagorejska trojka!")
    print()
    print("Enter numbers:")
    x = int(input())
    y = int(input())
    z = int(input())