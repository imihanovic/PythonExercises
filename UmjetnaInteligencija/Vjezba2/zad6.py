# -*- coding: utf-8 -*-
"""
Napisati funkciju koja prima listu brojeva. Funkcija provjerava da li se zbrajanjem 
ili oduzimanjem svih brojeva u listi može dobiti rezultat 0. Na primjer, za listu 
[ 1, 4, 5, 2, 4 ], funkcija vraća True (+1-4+5+2-4 = 0).
"""

def zbroji(lista, suma=0, i=0):
    
    if i == len(lista):
        return suma == 0
    if zbroji(lista, suma+lista[i], i+1):
        return True
    if zbroji(lista, suma-lista[i], i+1):
        return True

    return False

def main():
    lista = [1, 4, 5, 2]
    lista2 = [2, 6, 4]
    print(zbroji(lista))

if __name__ == '__main__':
    main()

def zbroji(lista, i, suma=0):
    print(i)
    if i < 0:
        return suma == 0
    if zbroji(lista, i-1, suma+lista[i]):
        return True
    if zbroji(lista, i-1, suma-lista[i]):
        return True

    return False

def main():
    lista = [1, 4, 5, 2]
    lista2 = [2, 6, 4]
    print(zbroji(lista2, len(lista2)-1))

if __name__ == '__main__':
    main()

