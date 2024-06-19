# -*- coding: utf-8 -*-
"""
funkciju koja za uneseni paran broj ispisuje sve različite načine na
koje se on može prikazati kao zbroj dva prosta broja. Pretpostavka
je da se svaki parni broj može napisati u obliku zbroja dva prosta
broja (Goldbachova slutnja).
"""
def checkIfPrime(x):
    if(x<=1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def goldbach():
    x = int(input())
    if(x%2!=0):
        x = int(input())
    for i in range(x):
        if(checkIfPrime(i) and checkIfPrime(x-i)):
            print(i, "+", x-i)
            
goldbach()
            
        

