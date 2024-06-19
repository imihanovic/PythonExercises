# -*- coding: utf-8 -*-
"""
U datoteci se u svakom retku nalaze dva cijela broja. Napisati funkciju
koja čita datoteku i sprema podatke u dictionary tako da je prvi broj u
retku ključ, a drugi broj element liste vrijednosti tog ključa.
"""
def readFile(f):
    dict={}
    for line in f.readlines():
        split = line.split(' ')
        key=int(split[0])
        val=int((split[1]).strip('\n'))
        if(key not in dict):
            dict[key]=[val]
        else:
            dict[key].append(val)
    return dict
        
f = open("brojevi.txt", "r")
dict = readFile(f)
print(dict)
f.close()

