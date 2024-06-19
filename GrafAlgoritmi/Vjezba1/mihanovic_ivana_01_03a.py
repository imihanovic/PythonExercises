# -*- coding: utf-8 -*-
"""
funkciju koja vraća koliko je prostih 
brojeva između dva decimalna broja
"""
def checkIfPrime(x):
    if(x<=1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def numberOfPrimeNumbers(x,y):
    cnt=0
    for i in range(x,y):
        if(checkIfPrime(i)):
            cnt+=1
    print("There are",cnt, "prime numbers")
x = round(float(input()))
y = round(float(input()))
print(x)
numberOfPrimeNumbers(x, y)

