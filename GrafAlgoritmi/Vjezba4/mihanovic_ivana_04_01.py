# -*- coding: utf-8 -*-
"""
Napisati funkcije koje će raditi konverzije zapisa grafa u matricu susjedstva, matricu incidencije i listu 
susjedstva grafa (iz svake strukture radi se konverzija u ostale dvije).
"""

from mihanovic_ivana_04_00 import main, printMatrica, matricaIncidencijeNeusmjerena, matricaIncidencijeUsmjerena
def getGraph():    
    return main()

def matricaSusjedstvaCreate(edges):
    matricaSusjedstva = []
    for i in range (len(vertices)):
        row = []
        for j in range (len(vertices)):
            for edge in edges:
                if(graph == "Neusmjeren"):
                    if [i+1,j+1].issubset(edge):
                        row.append(edges.count([i+1,j+1]))
                    elif [j+1,i+1].issubset(edge):
                        row.append(edges.count([j+1,i+1]))
                    else:
                        row.append(0)
                else:
                    if [i+1,j+1].issubset(edge):
                        row.append(edges.count([i+1,j+1]))
                    else:
                        row.append(0)
        matricaSusjedstva.append(row)
    return matricaSusjedstva
        
def listaSusjedstvaCreate(edges):
    listaSusjedstva = {}
    for i in range (len(vertices)):
        listaSusjedstva[vertices[str(i+1)]]=[]
        for j in range(len(edges)):
            if(graph == "Neusmjeren"):
                if(edges[j][0] == i+1):
                    listaSusjedstva[vertices[str(i+1)]].append(vertices[str(edges[j][1])])
                elif(edges[j][1] == i+1):
                    listaSusjedstva[vertices[str(i+1)]].append(vertices[str(edges[j][0])])
            else:
                if(edges[j][0] == i+1):
                    listaSusjedstva[vertices[str(i+1)]].append(vertices[str(edges[j][1])])
    # print(listaSusjedstva)
    return listaSusjedstva
                    
            
def incidencijaSusjedstvaLista():
    matricaSusjedstva = []
    listaSusjedstva = {}
    edges = []
    arcs = []
    for j in range (len(matricaIncidencije[0])):
        edge = []
        arc = []
        for i in range (len(matricaIncidencije)):
            if(graph == 'Neusmjeren'):
                if(matricaIncidencije[i][j]!=0):
                    edge.append(i+1)
                    if(len(edge)>1):
                        edge.append(matricaIncidencije[i][j])
            else:
                if(matricaIncidencije[i][j]<0):
                    arc.append(i+1)
                elif(matricaIncidencije[i][j]>0):
                    arc.insert(0, i+1)
                if(len(arc)>1):
                    arc.append(matricaIncidencije[i][j])
        if(graph == 'Neusmjeren'):
            edges.append(edge)
        else:
            arcs.append(arc)
    if(graph == "Neusmjeren"):
        matricaSusjedstva = matricaSusjedstvaCreate(edges)
        listaSusjedstva = listaSusjedstvaCreate(edges)
    else:
        matricaSusjedstva = matricaSusjedstvaCreate(arcs)
        listaSusjedstva = listaSusjedstvaCreate(arcs)
    return matricaSusjedstva, listaSusjedstva

def susjedstvaIncidencijaLista(matricaSusjedstva):
    matricaIncidencije = []
    listaSusjedstva = {}
    edges = []
    for i in range (len(matricaSusjedstva)):
        for j in range (len(matricaSusjedstva)):
            if(graph == "Neusmjeren"):
                if(matricaSusjedstva[i][j] > 0 and i<=j):
                    for k in range (matricaSusjedstva[i][j]):     
                        edges.append([i+1,j+1])
            else:
                if(matricaSusjedstva[i][j] > 0):
                    for k in range (matricaSusjedstva[i][j]):     
                        edges.append([i+1,j+1])
    if(graph == "Usmjeren"):
        matricaIncidencije = matricaIncidencijeUsmjerena(edges,len(vertices))
    else:
        matricaIncidencije = matricaIncidencijeNeusmjerena(edges, len(vertices))
    listaSusjedstva = listaSusjedstvaCreate(edges)
    return listaSusjedstva, matricaIncidencije
    
    
def listaIncidencijaSusjedstva(listaSusjedstva):
    matricaIncidencije = []
    matricaSusjedstva = []
    edges = []
    
    key_list = list(vertices.keys())
    val_list = list(vertices.values())
    for k, v in listaSusjedstva.items():
        for el in v:
            edges.append([int(key_list[val_list.index(k)]), int(key_list[val_list.index(el)])])
    if graph == 'Neusmjeren':
        unique = []
        for edge in edges:
            if edge[::-1] not in unique:
                unique.append(edge)
        matricaIncidencije = matricaIncidencijeNeusmjerena(unique, len(vertices))
        matricaSusjedstva = matricaSusjedstvaCreate(unique)
        return matricaIncidencije, matricaSusjedstva
    else:
        matricaIncidencije = matricaIncidencijeUsmjerena(edges, len(vertices))
        matricaSusjedstva = matricaSusjedstvaCreate(edges)
        return matricaIncidencije, matricaSusjedstva

matricaIncidencije, graph, vertices = getGraph()
#print(matricaIncidencije)
matricaSusjedstva, listaSusjedstva = incidencijaSusjedstvaLista()
# print()
printMatrica(matricaSusjedstva)
# print()
# print(listaSusjedstva)
# print()
# listaSusjedstva, matricaIncidencije = susjedstvaIncidencijaLista(matricaSusjedstva)
# print()
# matricaIncidencije, matricaSusjedstva = listaIncidencijaSusjedstva(listaSusjedstva) 
    
        