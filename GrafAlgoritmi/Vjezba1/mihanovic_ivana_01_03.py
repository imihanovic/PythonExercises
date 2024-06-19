# -*- coding: utf-8 -*-
"""
funkciju koja provjerava je li broj prost
"""
def checkIfPrime(x):
    if(x<=1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def numberOfPrimes():
    number = int(input()) 
    if(checkIfPrime(number)):
        print("Prime number: ", number)
    else:
        print("Not a prime number!")
        
numberOfPrimes()