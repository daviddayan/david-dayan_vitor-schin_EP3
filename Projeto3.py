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

#print(partes)

idade=float(partes[1])
peso=float(partes[2])
altura=float(partes[4])

if partes[3]=="M":
    TMB = 88.36 + (13.4 * peso) + (4.8 * altura*100) - (5.7 * idade)
elif partes[3]=="F":
    TMB = 447.6 + (9.2 * peso) + (3.1 * altura*100) - (4.3 * idade)
#print(TMB)

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
#print("numero de calorias ideal: ",x,"por dia")


consumo = usuario.readlines()

for i in range(len(consumo)):
    consumo[i] = consumo[i].strip()

for l in range(len(consumo)):
    consumo[l] = consumo[l].split(",")    
    
    

dic_consumo={}
consumo.remove(consumo[0])
#print(consumo)

for i in consumo:
    lista=[]
    lista.append(i[1])
    lista.append(i[2])
    dia=i[0]
    if dia not in dic_consumo:
        dic_consumo[dia] = []
    dic_consumo[dia].append(lista)

    
#print(dic_consumo)
   

abrir = open("alimentos.csv")
alimentos = abrir.readlines()

for i in range(len(alimentos)):
    alimentos[i] = alimentos[i].strip()

for l in range(len(alimentos)):
    alimentos[l] = alimentos[l].split(",")
alimentos.remove(alimentos[0])
#print(alimentos)

dic_alimentos={}
for l in alimentos:

    alim=l[0]
    if alim not in dic_alimentos:
        dic_alimentos[alim] = []
    dic_alimentos[alim].append(l[1])
    dic_alimentos[alim].append(l[2])
    dic_alimentos[alim].append(l[3])
    dic_alimentos[alim].append(l[4])
    dic_alimentos[alim].append(l[5])
    
#print(dic_alimentos)



consumo_total = {}

cal_por_grama=[]
for k in dic_consumo:
    tdia = 0
    for lista_dia in dic_consumo[k]:
        c=float(dic_alimentos[lista_dia[0]][1])
        g=float(dic_alimentos[lista_dia[0]][0])        
        tdia += float(lista_dia[1])*(c/g)
    consumo_total[k] = tdia

#print(consumo_total)
      

#calorias

consumo_total = {}


for k in dic_consumo:
    tdia = 0
    for lista_dia in dic_consumo[k]:
        c=float(dic_alimentos[lista_dia[0]][1])
        g=float(dic_alimentos[lista_dia[0]][0])        
        tdia += float(lista_dia[1])*(c/g)
    consumo_total[k] = tdia
    
#print(consumo_total)

datas=[]
for i in consumo_total:
    d=i.split("/")
    datas.append(d)
#print(datas)

import datetime

consumo_crono={}
d1=datetime.datetime(int(datas[0][2]), int(datas[0][1]), int(datas[0][0]))
d2=datetime.datetime(int(datas[1][2]), int(datas[1][1]), int(datas[1][0]))
d3=datetime.datetime(int(datas[2][2]), int(datas[2][1]), int(datas[2][0]))
d4=datetime.datetime(int(datas[3][2]), int(datas[3][1]), int(datas[3][0]))
d5=datetime.datetime(int(datas[4][2]), int(datas[4][1]), int(datas[4][0]))
d6=datetime.datetime(int(datas[5][2]), int(datas[5][1]), int(datas[5][0]))
d7=datetime.datetime(int(datas[6][2]), int(datas[6][1]), int(datas[6][0]))




    
#print(d1)
#print(d2)
#print(d3)
#print(d4)
#print(d5)
#print(d6)
#print(d7)



l_data=[d1,d2,d3,d4,d5,d6,d7]


cons2={}
j=0
for i in consumo_total:
        
    cons2[l_data[j]]=consumo_total[i]
    j+=1
#print(cons2)
num_dias = []

cal_dia=[]
for i in sorted(cons2):
    #print(cons2[i])
    cal_dia.append(cons2[i])
#print(cal_dia)

ordem_crono=sorted(l_data)

for d in ordem_crono:
    num_dias.append( (d - ordem_crono[0]).days )
#print(num_dias)

#proteinas

consumo_prot = {}

for k in dic_consumo:
    tdiaprot = 0
    for lista_dia in dic_consumo[k]:
        p=float(dic_alimentos[lista_dia[0]][2])
        g=float(dic_alimentos[lista_dia[0]][0])        
        tdiaprot += float(lista_dia[1])*(p/g)
    consumo_prot[k] = tdiaprot

#print(consumo_prot)

consprot={}
w=0
for i in consumo_prot:
        
    consprot[l_data[w]]=consumo_prot[i]
    w+=1
#print(consprot)

prot_dia=[]
for i in sorted(consprot):
    prot_dia.append(consprot[i])
#print(prot_dia)

#carboidratos

consumo_carb = {}

for k in dic_consumo:
    tdiacarb = 0
    for lista_dia in dic_consumo[k]:
        car=float(dic_alimentos[lista_dia[0]][3])
        g=float(dic_alimentos[lista_dia[0]][0])        
        tdiacarb += float(lista_dia[1])*(car/g)
    consumo_carb[k] = tdiacarb

#print(consumo_carb)

conscarb={}
z=0
for i in consumo_carb:
        
    conscarb[l_data[z]]=consumo_carb[i]
    z+=1
#print(conscarb)

carb_dia=[]
for i in sorted(conscarb):
    carb_dia.append(conscarb[i])
#print(carb_dia)

#gorduras

consumo_gord = {}

for k in dic_consumo:
    tdiagord = 0
    for lista_dia in dic_consumo[k]:
        gor=float(dic_alimentos[lista_dia[0]][4])
        g=float(dic_alimentos[lista_dia[0]][0])        
        tdiagord += float(lista_dia[1])*(gor/g)
    consumo_gord[k] = tdiagord

#print(consumo_gord)

consgord={}
ç=0
for i in consumo_gord:
        
    consgord[l_data[ç]]=consumo_gord[i]
    ç+=1
#print(consgord)

gord_dia=[]
for i in sorted(consgord):
    gord_dia.append(consgord[i])
#print(gord_dia)



import matplotlib.pyplot as plt

cal_id=[x]*7

#plt.plot(num_dias,prot_dia,"purple",label="proteinas")
#plt.legend(loc="upper right")
#plt.plot(num_dias,carb_dia,"y",label="carboidratos")
#plt.legend(loc="upper right")
#plt.plot(num_dias,gord_dia,"r",label="gorduras")
#plt.legend(loc="upper right")
#plt.axis(0,num_dias[6],0,500)
#plt.show()


plt.plot(num_dias,prot_dia,"purple",label="proteinas")
plt.legend(loc="upper right")
plt.plot(num_dias,carb_dia,"y",label="carboidratos")
plt.legend(loc="upper right")
plt.plot(num_dias,gord_dia,"r",label="gorduras")
plt.legend(loc="upper right")
plt.plot(num_dias,cal_id,"g",label="calorias")
plt.legend(loc="upper right")
plt.plot(num_dias,cal_dia,"b",label="calorias ideias")
plt.legend(loc="upper right")
plt.plot(num_dias,cal_dia,"p")
plt.axis(0,num_dias[6],0,cal_dia)
plt.show()




















