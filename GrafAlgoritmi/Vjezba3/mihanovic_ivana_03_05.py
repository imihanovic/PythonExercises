# -*- coding: utf-8 -*-
"""
Dan je dictionary kojem su ključevi brojevi, a vrijednosti liste brojeva.
Napisati funkciju koja okreće dictionary, na način da brojevi iz value listi
postaju keys, a keys postaju članovi value listi.
Primjer: Za d = {1:[2,3,5], 2:[1, 4], 3:[1,2]} novi dictionary je {1:[2,3],
2:[1,3], 3:[1], 4:[2], 5:[1]}
"""

dicti = {1:[2,3,5], 2:[1, 4], 3:[1,2,1]}
newDict={}

for k in dicti:
    for v in dicti[k]:
        if v in newDict:
            newDict[v].append(k)
        else:
            newDict[v] = [k]
newDict = dict(sorted(newDict.items()))
print(newDict)
