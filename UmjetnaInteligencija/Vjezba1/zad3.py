# -*- coding: utf-8 -*-
"""
Program koji za iduću jednadžbu traži cjelobrojno rješenje za x, y i z:  
    z/(x+y)+y/(z+x)+x/(z+y)=4
Program ispisuje sva rješenja za x, y i z u granicama -100 i 100.

"""
counter = 0
for x in range(-100,100):
    for y in range(-100,100):
        for z in range(-100,100):
            if (x+y)==0 or (y+z)==0 or (z+x)==0:
                continue
            if((z/(x+y))+(y/(z+x))+(x/(z+y)))==4:
                counter+=1
                print(x,y,z)                    
                
print(counter)