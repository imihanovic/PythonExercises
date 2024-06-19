# -*- coding: utf-8 -*-
"""
Napisati funkciju koja čita datoteku u kojoj je zapisan graf u pajek formatu i sprema
podatke o grafu u strukturu podataka po volji (matricu susjedstva, matricu incidencije
ili listu susjedstva grafa). 
MATRICA INCIDENCIJE
3 brida, 4 vrha
[[1 0 0],
 [0 1 0],
 [0 0 1],
 [1 1 1]
 ]

*Vertices     5
  1 "A"    
  2 "B"   
  3 "C"    
  4 "D"    
  5 "E"     
*Arcs
*Edges
  1 2 
  2 3 
  3 4
  1 4
  1 5
  2 4
  2 5
  4 5
"""
graph = False
tezinski = False
def printMatrica(matrica):
    for row in range(len(matrica)):
        for column in range(len(matrica[row])):
            print(matrica[row][column], end=" "*4)
        print()

def matricaIncidencijeUsmjerena(arcs, nrVertices):
    matrica_incidencije = []
    for i in range (int(nrVertices)):
        row = []
        for j in range (len(arcs)):
            edge1 = arcs[j]
            if(int(edge1[0])==(i+1)):
                if(len(edge1) == 3):
                    row.append(edge1[2])
                else:
                    row.append(edge1[1])
            elif(int(edge1[1])==(i+1)):
                if(len(edge1) == 3):
                    row.append(-edge1[2])
                else:
                    row.append(-1)
            else:
               row.append(0)
        matrica_incidencije.append(row)
        
    return matrica_incidencije

def matricaIncidencijeNeusmjerena(edges, nrVertices):
    matrica_incidencije = []
    for i in range (int(nrVertices)):
        row = []
        for j in range (len(edges)):
            edge1 = edges[j]
            if((int(edge1[0])==(i+1)) or (int(edge1[1])==(i+1))):
                if(len(edge1) == 3):
                   row.append(int(edge1[2]))
                else:
                   row.append(1)
            else:
                row.append(0)
        matrica_incidencije.append(row)
            
    return matrica_incidencije

def readPajek(f):
    dicti = {}
    dictKey = "Vertices"
    dicti[dictKey]={}
    for line in f:
        if ('Arcs' in line) or ('arcs' in line):
            dictKey = 'Arcs' 
            continue
        elif ('Edges' in line) or ('edges' in line):
            dictKey = 'Edges' 
            continue
        if(dictKey=='Vertices'):
            vert = line.split()
            if(len(vert) == 2):
                dicti[dictKey][vert[0]] = vert[1]
        elif(dictKey=='Arcs'):
            arc=line.split()
            if(len(arc) == 2): #BEZTEZINSKA
                if(dictKey in dicti):
                    dicti[dictKey].append([int(arc[0]), int(arc[1])])
                else:
                    dicti[dictKey] = [[int(arc[0]),int(arc[1])]]
            else: # TEZINSKA
                if(dictKey in dicti):
                    dicti[dictKey].append([int(arc[0]), int(arc[1]), int(arc[2])])
                else:
                    dicti[dictKey] = [[int(arc[0]),int(arc[1]),int(arc[2])]]
        elif(dictKey=='Edges'):
            ed=line.split()
            if(len(ed) == 2): #BEZTEZINSKA
                if(dictKey in dicti):
                    dicti[dictKey].append([int(ed[0]), int(ed[1])])
                else:
                    dicti[dictKey] = [[int(ed[0]),int(ed[1])]]
            else: # TEZINSKA
                if(dictKey in dicti):
                    dicti[dictKey].append([int(ed[0]), int(ed[1]), int(ed[2])])
                else:
                    dicti[dictKey] = [[int(ed[0]),int(ed[1]),int(ed[2])]]
    return dicti

def main():     
    f = open("pajek.txt", "r")
    nrVertices = f.readline().split()[1]
    dicti = readPajek(f)
    matrica = []
    graph = ""
    if('Arcs' in dicti):
        graph = "Usmjeren"
        matrica = matricaIncidencijeUsmjerena(dicti['Arcs'], nrVertices)
    else:
        graph = "Neusmjeren"
        matrica = matricaIncidencijeNeusmjerena(dicti['Edges'], nrVertices)
    return matrica, graph, dicti['Vertices']
if __name__ == '__main__':
    main()