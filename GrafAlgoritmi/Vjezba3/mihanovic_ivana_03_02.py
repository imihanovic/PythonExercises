# -*- coding: utf-8 -*-
"""
Napisati funkciju koja prima matricu sa cjelobrojnim elementima i vraća listu
u kojoj su elementi sume redaka u matrici.
"""

def listOfSums(matrix):
    sums=[]
    for i in range(len(matrix)):
        line=0
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int:
                return 0
            line+=matrix[i][j]
        sums.append(line)
    return sums
        
matrix = [[ 1, 0, 0, 0 ],
          [ -1, 1, 0, 0 ], 
          [ 1, 0, 0, 2 ],
          [ 0, 0, 0, 2 ]]

print(listOfSums(matrix))