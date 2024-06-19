# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:53:29 2023

@author: IvanaMihanović
"""

class Graph:
    def __init__(self, vertices=None, edges=None, directed=False):
        self.vertices = vertices or {}
        self.edges = edges or []
        self.directed = directed
    
    def __str__(self):
        return f'''
Graph:
Vertices {self.vertices}
Edges: {self.edges}
'''
def prim(g):
    #lista vrhova vrijednosti -1
    parent = [-1] * len(g.vertices)
    #lista maksimalnih vrijednosti
    key = [float('inf')] * len(g.vertices)
    #lista vrijednosti False, svaki vrh stvara li ciklus
    minimalnoRS = [False] * len(g.vertices)
    key[0] = 0
    
    #ZA BROJ BRIDOVA!
    for i in range(len(g.vertices) - 1):
        najmanjiKey = float('inf')
        
        #za svaki vrh, PROVJERA NAJMANJEG BRIDA
        for v in range(len(g.vertices)):
            if key[v] < najmanjiKey and not minimalnoRS[v]:
                najmanjiKey = key[v]
                najmanjiIndex = v
        minimalnoRS[najmanjiIndex] = True 
        
        #DODAJE BRID U KOJEM vrh iz brida je najmanji indeks i da ne stvara ciklus
        print()
        for edge in g.edges:
            v1, v2, tezina = edge
            if v1 == najmanjiIndex and not minimalnoRS[v2] and tezina < key[v2]:
                parent[v2] = najmanjiIndex
                key[v2] = tezina
    return parent

def kruskal(g):
    g.edges = sorted(g.edges, key=lambda el : el[2])
    parent = [-1] * len(g.vertices)
    kruskalEdges = []
    i = 0
    #PRETRAGA U DUBINU REKURZIVNO
    def provjeriCiklus(i):
        if parent[i] == -1:
            return i
        return provjeriCiklus(parent[i])
    
    #POSTAVLJANJE "RODITELJSKOG" VRHA od j NA VRH i
    def unija(x, y):
        parent[x] = y
    
    while len(kruskalEdges) < len(g.vertices) - 1:
        v1, v2, tezina = g.edges[i]
        i += 1
        #provjera postoji li ciklus
        x = provjeriCiklus(v1)
        y = provjeriCiklus(v2)
        #ako ne postoji, dodajemo brid
        if x != y:
            kruskalEdges.append([v1, v2, tezina])
            #setiramo novi roditeljski cvor
            unija(x, y)
    
    return kruskalEdges

def readf(fileName):
    f = open(fileName, "r")
    g = Graph()
    k = "vertices"
    for line in f.readlines():
        if('vertices' in line.lower()):
            splitVert = line.split()
            if(len(splitVert) == 2):
                vert, nrVertices = line.split()
            continue
        elif('arcs' in line.lower()):
            g.directed = True
            k = 'arcs'
            continue
        elif('edges' in line.lower()):
            g.directed = False
            k = 'edges'
            continue
        if k == 'vertices':
            l = line.split()  
            if(l[1] == ""):
                g.vertices[l[0]]="?"
            else:
                g.vertices[l[0]] = l[1]
        elif(k == 'arcs' or k=='edges'):
            l = line.split()
            g.edges.append([int(i) for i in l])
    print(g)
    return g

def main():
    g = readf('airports-split.net.txt')  
    primGraf = prim(g)
    print("Primov algoritam")
    for i in range(1, len(g.vertices)):
        print(primGraf[i],i)
    
    kruskalGraf = kruskal(g)
    print("\nKruskalov algoritam")
    for edge in kruskalGraf:
        print(edge[0], edge[1], edge[2])

if __name__ == '__main__':
    main()