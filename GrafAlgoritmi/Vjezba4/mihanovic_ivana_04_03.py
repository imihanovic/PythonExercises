# -*- coding: utf-8 -*-
"""
Napisati funkciju u kojoj se ispituje je li graf Eulerov
"""
from mihanovic_ivana_04_01 import getGraph
matricaIncidencije, graph, vertices = getGraph()
def isEuler(matricaIncidencije):
    for i in range(len(matricaIncidencije)):
        sum = 0
        for j in range(len(matricaIncidencije[0])):
            sum += abs(matricaIncidencije[i][j])
        if(sum%2 != 0):
            return False 
    return True

print(isEuler(matricaIncidencije))
    
