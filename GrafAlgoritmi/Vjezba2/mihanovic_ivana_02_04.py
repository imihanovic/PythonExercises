# -*- coding: utf-8 -*-
"""
Simulirati igru ”kamen, škare, papir”. Igrač igra protiv kompjutera. Igrač
bira jedno od ta tri pojma i dobija bod u svakom krugu ukoliko ima jači
alat. Pravila su:
· kamen pobjeđuje škare
· škare pobjeđuju papir
· papir pobjeđuje kamen
Koristiti containere za definiranje pravila igre.
"""
import random

lst = {1:"kamen",2:"skare",3:"papir"}
rules = {1:2,
         2:3,
         3:1}

player=0
comp=0
print("Unesite:\nKamen=1\nSkare=2\nPapir=3\nExit=0")
x = int(input())
y=random.randint(1,3)
print()
while(x<4 and x>=0):
    if(x==0):
        break
    if(x in rules and y==rules[x]):
        player+=1
        print("Player wins!")
    elif(y in rules and x==rules[y]):
        comp+=1
        print("Computer wins!")
    print("PLAYER:",lst[x],"- COMPUTER:", lst[y])
    print()
    print("PLAYER:",player)
    print("COMP:",comp)

    print()
    print("Unesite:\nKamen=1\nSkare=2\nPapir=3\nExit=0")
    x = int(input())
    y=random.randint(1,3)
    print()

            
