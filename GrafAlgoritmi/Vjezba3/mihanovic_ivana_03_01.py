# -*- coding: utf-8 -*-
"""
Napisati funkciju koja iz datoteke čita matricu sa cjelobrojnim elementima i vraća zbroj elemenata iznad glavne dijagonale i zbroj elemenata
iznad sporedne dijagonale. Ako matrica nije kvadratna, funkcija vraća
nule.
Primjer: Za matricu
2 4 6 8
5 3 4 6
1 3 5 6
0 3 5 7
funkcija vraća (34, 21).
"""
def suma(matrix):
    sumaGlavna=0
    sumaSporedna=0
    if(len(matrix[0]) != len(matrix)):
       return 0,0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(i<j):
                sumaGlavna+=matrix[i][j]
            if((i+j)<(len(matrix)-1)):
                sumaSporedna+=matrix[i][j]
    return sumaGlavna, sumaSporedna

def unosMatrice(f):
    mat=[]
    for line in f.readlines():
        mat.append([int (x) for x in line.split(' ')])
    return mat
        
f = open("kvadratnaMatrica.txt", "r")
matrix = unosMatrice(f)
glavna, sporedna=suma(matrix)
print("Glavna:", glavna, "\nSporedna:", sporedna)
f.close()


