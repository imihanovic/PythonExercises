# -*- coding: utf-8 -*-
"""
Napisati rekurzivnu verziju merge funkcije (bez petlji). Merge funkcija dobiva 
dvije sortirane liste i slaže sve elemente u novu sortiranu listu.
"""
def mergeRek(lst1, lst2):

    if(len(lst1)==0):
        return lst2
    
    if(len(lst2)==0):
        return lst1
    
    if(lst1[0]<lst2[0]):
        return [lst1.pop(0)]+ mergeRek(lst1, lst2)
    
    else:
        return [lst2.pop(0)]+ mergeRek(lst1, lst2)

print(mergeRek([1,3,5,7],[2,3,4,5,8,9]))
