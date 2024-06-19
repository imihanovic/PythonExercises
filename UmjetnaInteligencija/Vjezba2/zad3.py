# -*- coding: utf-8 -*-
"""
Napisati rekurzivnu funkciju za binarnu pretragu po listi brojeva. 
U implementaciji izbjeći bilo kakvo kopiranje liste ili dijela liste. 
To se može ostvariti prosljeđivanjem indeksa/granica liste/podliste.
"""

def findNumber(lst, lower, upper, br):
    
    trenutni = (upper+lower)//2
    print(lower, upper, trenutni)
    if(lst[trenutni] == br):
        return br
    elif lst[trenutni] > br:
        return findNumber(lst, lower, trenutni-1, br)
    else:
        return findNumber(lst, trenutni+1, upper, br)
    
    
lista = [1,25,99,87,16,32,11,12,99,101,122]
print(sorted(lista))

print(findNumber(sorted(lista), 0, len(lista)-1, 25))
