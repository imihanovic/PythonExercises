# -*- coding: utf-8 -*-
"""
Napisati rekurzivnu funkciju koja generira listu stringova koji 
predstavljaju sve moguće kombinacija slova „A“, „B“ i „C“. 
Dužina stringova je zadana kao parametar funkcije.
"""

def generiraj_kombinacije(n, kombinacija=''):
    if n == 0:
        return [kombinacija]
    else:
        print(kombinacija)
        kombinacije = []
        kombinacije.extend(generiraj_kombinacije(n - 1, kombinacija + 'A'))
        kombinacije.extend(generiraj_kombinacije(n - 1, kombinacija + 'B'))
        kombinacije.extend(generiraj_kombinacije(n - 1, kombinacija + 'C'))
        return kombinacije

sve_kombinacije = generiraj_kombinacije(3)
print(sve_kombinacije)
for kombinacija in sve_kombinacije:
    print(kombinacija)



