# -*- coding: utf-8 -*-
"""
Program koji sa korisnikom igra igru pogađanja broja: korisnik zamisli 
broju intervalu [0, 1000>, a  računalo pogađa broj. Računalo nakon 
pogađanja dobiva odgovor od korisnika: da li je „zamišljeni“ broj veći 
ili manji (> ili <) od predloženog broja. Program dolazi do zamišljenog 
broja u najmanjem broju pogađanja (koristeći sličnu ideju kao binarna pretraga). 
Program završava kada je broj pogođen. 
"""

def guessNumber(lower, upper):
    guess = (upper+lower)//2
    print(guess)
    user = input("<,> or Y: ")
    if(user == "Y"):
        return True
    if(user == "<"):
        return guessNumber(lower, guess)
    elif(user == ">"):
        return guessNumber(guess, upper)

guessNumber(0,1000)