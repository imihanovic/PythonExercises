# -*- coding: utf-8 -*-
"""
Napisati funkciju prima matricu sa cjelobrojnim elementima i provjerava
ima li matrica točno dvije jedinice u svakom stupce, a ostale elemente
stupca nula. Ako postoji stupac koji ne zadovoljava taj uvjet, funkcija
vraća False, inače True.
"""
def checkForOnes(matrix):
    numberOf = len(matrix[0])
    for j in range(numberOf):
        cnt=0
        for i in range(len(matrix)):
            if matrix[i][j] == 1:
                cnt+=1
            elif matrix[i][j]!=0:
                return False
        if cnt!=2:
            return False
        cnt=0
    return True

matrix = [[ 1, 0, 1, 1 ],
          [ 0, 1, 0, 0 ], 
          [ 1, 0, 1, 1 ],
          [ 0, 1, 0, 0 ],
          [ 0, 0, 0, 0]]

print(checkForOnes(matrix))