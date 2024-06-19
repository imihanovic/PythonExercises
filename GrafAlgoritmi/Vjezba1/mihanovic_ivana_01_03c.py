# -*- coding: utf-8 -*-
"""
funkciju koja ispisuje i vraća sve susjedne proste brojeve do n. Za
dva prosta broja kažemo da su susjedni ako im je razlika jednaka 2.
"""
def checkIfPrime(x):
    if(x<=1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def neighbourNumbers(x):
    x = int(input())
    i = 2
    while(i<=x):
        if(checkIfPrime(i) and checkIfPrime(i+2)):
           print(i,i+2)
        i+=1
    
neighbourNumbers()
