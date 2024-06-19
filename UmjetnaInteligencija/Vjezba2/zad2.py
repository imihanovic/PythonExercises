# -*- coding: utf-8 -*-
"""

Napisati rekurzivno rješenje za zadatak iz prve vježbe. Napisati funkciju 
koja za dva primljena broja sa jednakim brojem znamenaka, provjerava da li 
su brojevi sastavljeni od istih znamenaka (npr. 32451 i 25123). Cijelo rješenje 
mora biti bez implementirano bez petlji, odnosno samo pomoću rekurzivnih funkcija. 

"""
def provjeri(znamenka, br):
    if not br:
        return False
    if(znamenka == br%10):
        return True
    return provjeri(znamenka, br//10)
    

def rekurzivna(a, b):
    if a<10:
        return provjeri(a, b)  
    elif not provjeri(a%10, b):
        return False
    else:
        return rekurzivna(a//10, b)
    
def glavnaFunkcija(a, b):
    
    if(len(str(a))!=len(str(b))):
        return False
    
    if rekurzivna(a,b) and rekurzivna(b,a):
        return True
    else:
        return False


print(glavnaFunkcija(123455, 512234))
print(glavnaFunkcija(123455, 516234))
print(glavnaFunkcija(12346, 512234))
print(glavnaFunkcija(123467, 716234))
print(glavnaFunkcija(123333, 122331))
print(glavnaFunkcija(123333, 122431))
