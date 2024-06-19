# -*- coding: utf-8 -*-
"""
Algoritam sortiranih bridova
"""
from readCSV import *
from time import time
from collections import defaultdict
 

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
     
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)
    
    def removeEdge(self, v, w):
        self.graph[v].remove(w)
        self.graph[w].remove(v)
     
    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
            elif parent != i:
                return True
        return False
     
    def isCyclic(self):
        visited = [False]*(self.V)
        for i in range(self.V):
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, -1)) == True:
                    return True
        return False
    
        
def degreeThree(verts, edge):
    v1 = edge[0]
    v2 = edge[1]
    if v1 in verts and verts[v1] == 2:
        return True
    elif v2 in verts and verts[v2] == 2:
        return True
    return False

def lista(matricaSusjedstva):
    
    g = Graph(len(matricaSusjedstva))
    edges = []
    verts = {}
    result = []
    for i in range(len(matricaSusjedstva)):
        for j in range(len(matricaSusjedstva[0])):
            if(i<j):
                edges.append((i,j,matricaSusjedstva[i][j]))
    edges.sort(key = lambda x: x[2]) 
    #print(edges)
    while len(verts) < len(matricaSusjedstva):
        if len(edges) == 0:
            break
        edge = edges[0]
        g.addEdge(edge[0],edge[1])
        if not g.isCyclic():
            #print("Graph doesn't contain cycle ")
            if not degreeThree(verts, edge):
                if edge[0] in verts:
                    verts[edge[0]] += 1
                else:
                    verts[edge[0]] = 1
                if edge[1] in verts:
                    verts[edge[1]] += 1
                else:
                    verts[edge[1]] = 1
                result.append(edge)
        else:
            #print("Graph contains cycle")
            g.removeEdge(edge[0], edge[1])
        del edges[0]
    #print(edges)
    print(verts) 
    keys = sorted([k for k, v in verts.items() if v == 1])
    #print(result)
    for e in edges:
        if(keys[0] == e[0] and keys[1] == e[1]):
            result.append(e)
    print(result)
def main():
    start = time()
    vertices, matricaSusjedstva = matricaSusjedstvaF('distance.csv')
    lista(matricaSusjedstva)
    end = time()
    print("Vrijeme izvrsavanja: ", end-start)
if __name__ == '__main__':
    main()

