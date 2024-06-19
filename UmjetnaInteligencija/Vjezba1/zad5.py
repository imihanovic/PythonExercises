# -*- coding: utf-8 -*-
"""
Program koji sa korisnikom igra igru pogađanja broja: računalo generira 
slučajni broj u intervalu [0, 1000> i pita korisnika da ga pogodi. Računalo 
nakon svakog pogađanja odgovara da li je „zamišljeni“ broj veći ili manji od
korisnikovog broja. Program završava kada je broj pogođen.
"""

from random import randint
guess = False
broj = randint(0, 1000)
while not guess:
    br = int(input("Unesi broj: "))
    if(br == broj):
        print("Broj je pogoden!")
        guess = True
    elif(br > broj):
        print("Broj je manji od unesenog!")
    else:
        print("Broj je veći od unesenog!")