# -*- coding: utf-8 -*-
"""
funkciju koja vraća n-ti prosti broj,
"""
def checkIfPrime(x):
    if(x<=1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def returnPrimeN():
    x = int(input())
    cnt = 0
    i = 2
    while(True):
        if(checkIfPrime(i)):
            cnt+=1
        if(cnt==x):
            print(i)
            break
        i+=1
    
returnPrimeN()