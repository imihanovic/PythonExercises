# -*- coding: utf-8 -*-
"""
Algoritam najblizeg susjeda
"""
from readCSV import *
from time import time
import random

def getDistances (verts, row):
    row.sort(key = lambda x: x[1])
    notAdded = True
    i = 0
    while notAdded:
        if(row[i][0] not in verts):
            verts.append(row[i][0])
            notAdded = False
        else:
            i+=1
    print(row)
    print(verts)
    
def cna(vertices, matricaSusjedstva):
    randomV = random.choice(vertices)
    print(randomV)
    verts = [randomV[0]]
    while len(verts) != len(vertices):
        row = []
        for d in range(len(matricaSusjedstva)):
            row.append((d,matricaSusjedstva[verts[-1]][d]))
        getDistances(verts, row)
    verts.append(randomV[0])
    print(verts)
        
def main():
    start = time()
    vertices, matricaSusjedstva = matricaSusjedstvaF('distance.csv')
    printMatrica(matricaSusjedstva)
    cna(vertices, matricaSusjedstva)
    end = time()
    print("Vrijeme izvrsavanja: ", end-start)
if __name__ == '__main__':
    main()