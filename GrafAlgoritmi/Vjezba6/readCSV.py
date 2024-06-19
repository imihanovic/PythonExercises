# -*- coding: utf-8 -*-
import csv

def printMatrica(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            print(matrica[i][j],end = " ")
        print()
        
def matricaSusjedstvaF(path):
    with open(path, newline='') as csvfile:
        global reader
        reader = csv.DictReader(csvfile)
        matricaSusjedstva = []
        vertices = []
        cnt = 0
        for row in reader:
            newRow = []
            for element in row:
                if element == '':
                    vertices.append((cnt,row['']))
                    cnt += 1
                else:
                    # print(element)
                    if row[element] != '-':
                    # if(element != row['']):
                        newRow.append(int(row[element]))
                    else:
                        newRow.append(0)
            matricaSusjedstva.append(newRow)
        return vertices, matricaSusjedstva
    

