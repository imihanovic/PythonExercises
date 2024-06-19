# -*- coding: utf-8 -*-
"""
BRUTE-FORCE
"""
from readCSV import *
from time import time

def isSafe(v, graph, path, pos):
	if graph[path[pos - 1]][v] == 0:
		return False
    
	for i in range(pos):
		if path[i] == v:
			return False
	return True

hasCycle = False
cycles = []

def hamCycle(graph):
    global hasCycle
    hasCycle = False

    path = []
    path.append(0)

    visited = [False]*(len(graph))
    visited[0] = True

    FindHamCycle(graph, 1, path, visited)

    if hasCycle:
        print("No Hamiltonian Cycle" + "possible ")
        return

def FindHamCycle(graph, pos, path, visited):
    global cycles
    if pos == len(graph):
        if graph[path[-1]][path[0]] != 0:
            path.append(0)
            
            one = []
            for i in range(len(path)):
                one.append(path[i])
            cycles.append(one)
            path.pop()
            hasCycle = True
        return
    
    for v in range(len(graph)):
        if isSafe(v, graph, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True
            FindHamCycle(graph, pos + 1, path, visited)
            visited[v] = False
            path.pop()

def getSmallestCycle(uniqueCycles, matricaSusjedstva):
    dist = []
    for i in range(len(uniqueCycles)):
        cycle = uniqueCycles[i]
        suma = 0
        for j in range(len(cycle)-1):
            first = cycle[j]
            second = cycle[j+1]
            suma += int(matricaSusjedstva[first][second])
        dist.append((suma,cycle))
    #print(sorted(dist))
    return sorted(dist)[0]

def main():
    start = time()
    vertices, matricaSusjedstva = matricaSusjedstvaF('distance.csv')
    hamCycle(matricaSusjedstva)
    uniqueCycles = cycles[:len(cycles)//2]
    smallest = getSmallestCycle(uniqueCycles, matricaSusjedstva)
    for i in range(len(smallest[1])-1):
        print(smallest[1][i], " -> ",end = "")
    print(smallest[1][-1])
    end = time()
    print("Vrijeme izvrsavanja: ", end-start)
if __name__ == '__main__':
    main()

