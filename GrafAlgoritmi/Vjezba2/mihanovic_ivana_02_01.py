# -*- coding: utf-8 -*-
"""
Napisati funkciju koja za dvije liste vraća listu koja se sastoji 
od elemenata koji se nalaze u obje liste bez iteriranja po listama.
"""

def obje(lst1, lst2):
    print(list(set(lst1).intersection(lst2)))

lst1=[1,2,3,1,2,5,6]
lst2=[3,4,1,7,2,8,9]
obje(lst1,lst2)