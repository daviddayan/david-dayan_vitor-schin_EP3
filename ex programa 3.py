# -*- coding: utf-8 -*-
usuario = open("usuario.csv",encoding="utf-8")
usuario.readline()
linhas = usuario.readline()
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

def caloria_ideal(a):
    if a=="minimo\n":
        return(1.2*TMB)
    elif a=="baixo":
        return(1.375*TMB)
    elif a=="medio":
        return(1.55*TMB)
    elif a=="alto\n":
        return(1.725*TMB)
    elif a=="muito alto":
        return(1.9*TMB)

x=caloria_ideal(partes[5])
print("numero de calorias ideal: ",x,"por dia")

usuario.readline()
consumo = usuario.readline()
cons = consumo.split(",")
dic={}
dic[cons[0]]=[cons[1],cons[2]]
print(cons)
print(dic)