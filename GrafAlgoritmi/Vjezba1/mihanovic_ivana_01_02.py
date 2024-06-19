# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:09:34 2023

@author: IvanaMihanović

Napisati funkciju koja će za prirodan broj n < 20 ispisati brojevni trokut
prema sljedećem primjeru (za n = 9):
1
2 3 2
3 4 5 4 3
4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
6 7 8 9 0 1 0 9 8 7 6
7 8 9 0 1 2 3 2 1 0 9 8 7
8 9 0 1 2 3 4 5 4 3 2 1 0 9 8
9 0 1 2 3 4 5 6 7 6 5 4 3 2 1 0 9

"""

def triangle(lst):
    print()
    for i in range(1,len(lst)):
        row=[]
        row.append(i%10)
        k=(i%10)+1
        for j in range(i-1):
            if(k>9):
                k=0
            row.append(k)
            k+=1
        print(*row, end=" ")
        row.reverse()
        row.pop(0)
        print(*row, end=" ")
        print()
    
n = int(input())
lst = []
for i in range(n+1):
    lst.append(i)
triangle(lst)