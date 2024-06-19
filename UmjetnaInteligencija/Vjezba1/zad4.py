# -*- coding: utf-8 -*-
"""
Napisati program koji za dva unesena broja sa jednakim brojem znamenaka, 
provjerava da li su brojevi sastavljeni od istih znamenaka (npr. 32451 i 25123).
"""

a = int(input("Prvi: "))
b = int(input("Drugi: "))

if(len(str(a))) != len(str(b)):
    print("Brojevi su razlicite duljine!")
    
elif sorted(set(str(a))) == sorted(set(str(b))):
    print("Brojevi se sastoje od istih znamenki!")
    
else:
     print("Brojevi se ne sastoje od istih znamenki!")
    
        