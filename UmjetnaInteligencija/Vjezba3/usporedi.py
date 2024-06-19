# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:12:48 2024

@author: IvanaMihanović
"""
from Igra import Briskula, Bot, Human, Igrac

def igraj(N):
    igrac1W, igrac2W, neodluceno = 0, 0, 0
    
    for i in range(N):
        briskula = Briskula(Igrac("ivana"),Bot())
        rezultat = briskula.odigraj_partiju()
        if rezultat == 1:
            igrac1W +=1
        elif rezultat == 2:
            igrac2W +=1
        else:
            neodluceno +=1
        
    # for j in range(N//2):
    #     briskula = Briskula(Bot(),Bot())
    #     rezultat = briskula.odigraj_partiju()
    #     if rezultat == 1:
    #         igrac1W +=1
    #     elif rezultat == 2:
    #         igrac2W +=1
    #     else:
    #         neodluceno +=1
        
    print(f"Pobjede -> igrac1: {igrac1W}, igrac2: {igrac2W}, neodlucene: {neodluceno}. ")
    print()
        

igraj(1000)

