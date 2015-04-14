# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:24:07 2015

@author: vitorkitahara
"""

usuario = open("usuario.csv",encoding="utf-8")
usuario.readline()
linhas = usuario.readline()
linhas = linhas.strip()
partes = linhas.split(",")

print(partes)

idade=float(partes[1])
peso=float(partes[2])
altura=float(partes[4])

if partes[3]=="M":
    TMB = 88.36 + (13.4 * peso) + (4.8 * altura*100) - (5.7 * idade)
elif partes[3]=="F":
    TMB = 447.6 + (9.2 * peso) + (3.1 * altura*100) - (4.3 * idade)
print(TMB)

str.strip(partes[5].strip())
def caloria_ideal(a):
    if a=="minimo":
        return(1.2*TMB)
    elif a=="baixo":
        return(1.375*TMB)
    elif a=="medio":
        return(1.55*TMB)
    elif a=="alto":
        return(1.725*TMB)
    elif a=="muito alto":
        return(1.9*TMB)

x=caloria_ideal(partes[5])
print("numero de calorias ideal: ",x,"por dia")


consumo = usuario.readlines()

for i in range(len(consumo)):
    consumo[i] = consumo[i].strip()

for l in range(len(consumo)):
    consumo[l] = consumo[l].split(",")    
    
    
dic={}
consumo.remove(consumo[0])
print(consumo)
for i in consumo:
    lista=[]
    lista.append(i[1])
    lista.append(i[2])
    dia=i[0]
    if dia not in dic:
        dic[dia] = []
    dic[dia].append(lista)
    
print(dic)

