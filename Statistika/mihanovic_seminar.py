# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy import stats

data = (pd.read_excel('p9.xlsx')['Trajanje simptoma \nbolesti/dani'].tolist())
dataF = pd.DataFrame(data, columns=['Dani'])

prazna = []
for i in range(len(data)):
    prazna.append(round(data[i]))
print(prazna)
# Aritmeticka sredina
srednjaVrijednost = dataF['Dani'].mean()
print("Srednja vrijednost:", srednjaVrijednost)

# Mod
print("Mod:", dataF['Dani'].mode()[0])

# Medijan
medijan = dataF['Dani'].median()
print("Medijan:", medijan)

# Dodatni podaci potrebni za karakteristicnu petorku, raspon i interkvartil
min = (dataF['Dani'].min())
max = (dataF['Dani'].max())

# Karakteristicna petorka
print("Karakteristična petorka:", min, dataF['Dani'].quantile(0.25), medijan, dataF['Dani'].quantile(0.75), max)

# Varianca
print("Varijanca:", dataF['Dani'].var())

# Standardna devijacija
standardnaDevijacija = dataF['Dani'].std()
print("Standardna devijacija:", standardnaDevijacija)

# Interkvartil
print("Interkvartil:", stats.iqr(dataF['Dani']))

# Raspon
raspon = max-min
print("Raspon uzorka:", raspon)


#FREKVENCIJE, GRANICE

frekvencije, granice = np.histogram(dataF['Dani'], bins = 7)
for i in range(len(granice)):
    granice[i] = round(granice[i], 2)
    
relativneF = frekvencije / frekvencije.sum()
kumulativneF = np.cumsum(relativneF)
dataFfrekvencije = pd.DataFrame({'Frekvencija':frekvencije, 'Razred': granice[:-1]})

#RAZDIOBA FREKVENCIJA
sveFrekvencije = pd.DataFrame({'Razred':pd.IntervalIndex.from_arrays(granice[:-1],granice[1:]),'f':frekvencije, 'Relativne f': relativneF, 'Kumulativne relativne f':kumulativneF})
print()
print(sveFrekvencije)

bin_count = math.ceil(math.sqrt(len(dataF['Dani'])))
bin_edges = np.linspace(dataF['Dani'].min(),dataF['Dani'].max(), 8)

#HISTOGRAM F
plt.hist(dataF['Dani'],bins=7, edgecolor='black')
plt.title('Histogram frekvencija')
plt.show()



#Histogram relativnih frekvencija
plt.hist(dataF['Dani'], bins=bin_edges, edgecolor='black' ,weights=np.ones_like(dataF['Dani']) / len(dataF['Dani']))
plt.title('Histogram relativnih frekvencija')
plt.show()

#POLIGON

plt.plot(dataFfrekvencije['Razred'], relativneF, marker = 'o', linestyle = '-', color="red")
plt.title('Poligon frekvencija')
plt.show()
print()

#INTERVAL POVJERENJA
pouzdanost = 0.90
intervalPovjerenja = stats.norm.interval(pouzdanost, loc = srednjaVrijednost, scale = standardnaDevijacija/np.sqrt(len(dataF['Dani'])))
print("Pouzdanost: ", pouzdanost)
print("Interval povjerenja: ", intervalPovjerenja)

pouzdanost = 0.95
intervalPovjerenja = stats.norm.interval(pouzdanost, loc = srednjaVrijednost, scale = standardnaDevijacija/np.sqrt(len(dataF['Dani'])))
print("Pouzdanost: ", pouzdanost)
print("Interval povjerenja: ", intervalPovjerenja)

pouzdanost = 0.99
intervalPovjerenja = stats.norm.interval(pouzdanost, loc = srednjaVrijednost, scale = standardnaDevijacija/np.sqrt(len(dataF['Dani'])))
print("Pouzdanost: ", pouzdanost)
print("Interval povjerenja: ", intervalPovjerenja)

#HIPOTEZA
print()
uzorak = 15
t_statistic, p_value = stats.ttest_1samp(data, uzorak)
print("Tstatistika:", t_statistic)
print("Pvalue:", p_value)