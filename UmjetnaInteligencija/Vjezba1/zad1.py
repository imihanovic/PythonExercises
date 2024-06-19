# -*- coding: utf-8 -*-
"""
1.	Napisati funkcije koje rade sa vektorima koji su predstavljeni kao liste brojeva:
a.	Zbroj dva vektora
b.	Umnožak vektora i broja
c.	Umnožak dvaju vektora (xxT, rezultat je broj)
d.	Umnožak dvaju vektora (xTx, rezultat je matrica)

"""
def zbrojVektora(v1, v2):
    if(len(v1)!=len(v2)):
        print("Vektori su razlicitih duljina")
        return
    print([sum(el) for el in zip(v1, v2)])
    
def umnozakVektoraIBroja(v1, br):
    print([el * br for el in v1])
    
def umnozakVektoraBroj(v1,v2):
    if(len(v1)!=len(v2)):
        print("Vektori su razlicitih duljina")
        return
    result = 0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
    print(result)

def umnozakVektoraMatrica(v1,v2):
    print([[x * y for y in v2] for x in v1])
    
    
def main():
    v1 = [1,2,3]
    v2 = [4,5,6]
    
    zbrojVektora(v1,v2)
    umnozakVektoraIBroja(v1, 7)
    print()
    umnozakVektoraBroj(v1,v2)
    umnozakVektoraMatrica(v1,v2)
    
if __name__ == '__main__':
    main()