# -*- coding: utf-8 -*-
"""
Napisati count funkciju. Funkcija prima listu i predikat i vraća koliko 
elemenata u listi zadovoljava predikat. Predikat je funkcija koja prima 
jedan element liste i vraća True / False. Napisati iterativnu i rekurzivnu 
verziju funkcije.
"""
def iterativna(lst, predikat):
    cnt=0
    for i in lst:
        if(predikat(i)):
            cnt+=1
    print(cnt)
    
iterativna([1,2,3,4,5,6,7,8], lambda x:x%2==0)

def rekurzivna(lst, predikat):
    if(len(lst)==0):
        return 0
    br = lst[-1]
    lst.pop()
    if(predikat(br)):
        return 1 + rekurzivna(lst,predikat)
    else:
        return 0 + rekurzivna(lst,predikat)
    
print(rekurzivna([1,2,3,4,8,6,7,8], lambda x:x%2==0))
    
