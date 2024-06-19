# -*- coding: utf-8 -*-
"""
Napisati iterativnu i rekurzivnu funkciju koja za listu vraća element
najveće brojčane vrijednosti. Vrijednosti u listi koji nisu brojevi ignorira.
Primjer: Za listu lst = [7, 18, 3, 'a', True, (2,3)] funkcija vraća 18.
"""

def iter(lst):
    lst = [num for num in lst if type(num) in (float, int)]
    maximum = lst[0]
    for i in range (len(lst)):
        if(lst[i]>maximum):
            maximum = lst[i]
    return maximum

def recurs(lst, length):
    if (length == 1):
        return lst[0]
    return max(lst[length - 1], recurs(lst, length - 1))
    
lst=[7, 18, 3, 'a', True, (2,3)]
lst2=[1,20,'ncfjdsndkf',False,-6,31,[4,5,2]]
lstNumbers = [num for num in lst if type(num) in (float, int)]
lst2Numbers = [num for num in lst2 if type(num) in (float, int)]
print(iter(lst))
print(recurs(lstNumbers, len(lstNumbers)))
print()
print(iter(lst2))
print(recurs(lst2Numbers, len(lst2Numbers)))