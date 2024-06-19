# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:26:12 2023

@author: IvanaMihanović
"""

class Graph:  
    
    def __init__(self, vertices):  
        self.vertices = vertices  
        self.edges = []  
        self.adjacencyList = {v: [] for v in vertices}  
  
    def addEdge(self, v1, v2, weight):  
        self.edges.append((v1, v2, weight))  
        self.adjacencyList[v1].append((v2, weight))  
        self.adjacencyList[v2].append((v1, weight))  
  
    def findRoot(self, root, i):  
        if root[i] == i:  
            return i  
        return self.findRoot(root, root[i])  
  
    def union(self, root, stupanj, x, y):  
        rootX = self.findRoot(root, x)  
        rootY = self.findRoot(root, y)  
        if stupanj[rootX] < stupanj[rootY]:  
            root[rootX] = rootY  
        elif stupanj[rootX] > stupanj[rootY]:  
            root[rootY] = rootX  
        else:  
            root[rootY] = rootX  
            stupanj[rootX] += 1  
  
    def kruskal(self):  
        result = set()  
        root = {}  
        stupanj = {}  
        for v in self.vertices:  
            root[v] = v  
            stupanj[v] = 0  
        edgesSorted = sorted(self.edges, key=lambda x: x[2])  
        for edge in edgesSorted:  
            v1, v2, weight = edge  
            rootV1 = self.findRoot(root, v1)  
            rootV2 = self.findRoot(root, v2)  
            if rootV1 != rootV2:  
                result.add(edge)  
                self.union(root, stupanj, rootV1, rootV2)  
        return result  
vertices = []
edges = []

def readPajek(f):
    f.readline()
    dicti = {}
    dictKey = "Vertices"
    dicti[dictKey] = []
    for line in f.readlines():
        l = line.split()
        if 'edges' in line:
            dictKey = 'Edges'
            continue
        if dictKey == "Vertices":
            vertices.append(int(l[0]))
        elif dictKey == "Edges":
            if((int(l[1]),int(l[0]),int(l[2])) not in edges):
                edges.append((int(l[0]),int(l[1]),int(l[2])))
    return dicti
f = open("airports-split.net.txt", "r")
dicti = readPajek(f)
g = Graph(vertices) 
for i in range(len(edges)):
    edge = edges[i]
    g.addEdge(edge[0],edge[1],edge[2]) 
result = g.kruskal()  
print(result)