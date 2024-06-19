# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:34:35 2023

@author: IvanaMihanović
"""
import sys
 
 
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
 
    def minKey(self, key, mstSet):
        min_index = 0
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1
 
        for cout in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
 
        self.printMST(parent)
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
            edges.append([int(l[0]),int(l[1]),int(l[2])])
    return dicti

f = open("airports-split.net.txt", "r")
dicti = readPajek(f)
g = Graph(len(vertices)) 
def printMatrica(matrica):
    for row in range(len(matrica)):
        print(matrica[row], end=" "*5)
        print()
        
def matricaSusjedstvaCreate(edges):
    matricaSusjedstva = []
    for i in range(len(vertices)):
        row = []
        for j in range(len(vertices)):
            row.append(0)
        matricaSusjedstva.append(row)
    for edge in edges:
        matricaSusjedstva[edge[0]][edge[1]] = edge[2]
    return matricaSusjedstva

g.graph = matricaSusjedstvaCreate(edges)
g.primMST()