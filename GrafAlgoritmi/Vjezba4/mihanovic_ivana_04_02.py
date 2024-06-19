# -*- coding: utf-8 -*-
"""
Napisati funkcije koje računaju:
— broj vrhova u grafu
— broj bridova u grafu
— stupanj svakog vrha
— vrhove s maksimalnim brojem incidentnih bridova
"""
from mihanovic_ivana_04_01 import getGraph, printMatrica, incidencijaSusjedstvaLista

matricaIncidencije, graph, vertices = getGraph()
matricaSusjedstva, listaSusjedstva = incidencijaSusjedstvaLista()

def nOfVertices(matricaIncidencije):
    return len(matricaIncidencije)

def nOfEdges(matricaIncidencije):
    return len(matricaIncidencije[0])

def vertDegree(listaSusjedstva):
    degrees = {}
    for k, v in listaSusjedstva.items():
        degrees[k] = len(v)
    return degrees

def maxVertDegree(listaSusjedstva):
    max = 0
    maxVert = {}
    for k, v in listaSusjedstva.items():
        if len(v)>max:
            max = len(v)
    maxVert[max] = []
    for k, v in listaSusjedstva.items():
        if(len(v) == max):
            maxVert[max].append(k)
    return maxVert

print(nOfVertices(matricaIncidencije))
print(nOfEdges(matricaIncidencije))
print(vertDegree(listaSusjedstva))
print(maxVertDegree(listaSusjedstva))

