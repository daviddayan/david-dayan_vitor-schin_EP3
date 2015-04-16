# -*- coding: utf-8 -*-
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
    
print(dic_consumo)
   

abrir = open("alimentos.csv")
alimentos = abrir.readlines()

for i in range(len(alimentos)):
    alimentos[i] = alimentos[i].strip()

for l in range(len(alimentos)):
    alimentos[l] = alimentos[l].split(",")
alimentos.remove(alimentos[0])
#print(alimentos)


#def divisao():
#    cal_por_grama=[]   
#    for i in alimentos:
#        g=float(i[1])
#        c=float(i[2])
#        cal_por_g=(c/g)
#        cal_por_grama.append(cal_por_g)
#    return cal_por_grama
#x=divisao()    
#print(x)

dic_alimentos={}
for l in alimentos:
#    lista2=[]
#    lista2.append(l[1])
#    lista2.append(l[2])
    alim=l[0]
    if alim not in dic_alimentos:
        dic_alimentos[alim] = []
    dic_alimentos[alim].append(l[1])
    dic_alimentos[alim].append(l[2])
print(dic_alimentos)



consumo_total = {}

cal_por_grama=[]
for k in dic_consumo:
    tdia = 0
    for lista_dia in dic_consumo[k]:
        c=float(dic_alimentos[lista_dia[0]][1])
        g=float(dic_alimentos[lista_dia[0]][0])        
        tdia += float(lista_dia[1])*(c/g)
    consumo_total[k] = tdia

print(consumo_total)
      

    
        
        
        
        
        
        
    




        


