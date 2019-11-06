#!/usr/bin/env python
# Name: GUI.py
# Purpose: GUI para o perceptron 
# Author: Tiago Bockholt <tiagobockholt@gmail.com>

#importa as bibliotecas
from Perceptron import Perceptron
from pylab import *
   
#Inicio da Rotina Principal

pesos = [0.2,0.3,0.4]
data = [(-1,0,0),(-1,0,1),(-1,1,0),(-1,1,1)]
dclasse = [0,1,0,0]
#taxa de aprendizagem
n=0.3

p = Perceptron(pesos, data, dclasse, n)

#parametros para plotar a reta do tipo alfa*x + beta   
alfa,beta = p.treinaPerceptron()

#processar os dados pra plotar
listax0=[]
listay0=[]
listax1=[]
listay1=[]

for i,classe in enumerate(dclasse):
    if classe==0:
        listax0.append(data[i][1])
        listay0.append(data[i][2])
        
    else:
        listax1.append(data[i][1])
        listay1.append(data[i][2])
            
 


### GUI propriamente dita
#dominio(min,max,CTE)
min=min(min(listax0),min(listax1),min(listay0),min(listay1))

max=max(max(listax0),max(listax1),max(listay0),max(listay1))


x = arange(min-1, max+1, 0.1)

axis([min-1, max+1, min-1, max+1])

xlabel('X')
ylabel('Y')

title('Perceptron Classification')
#plotagem do hiperplano de classificao
plot(x, alfa*x + beta, 'r')

#plotagem dos padroes da classe 0
#plot([0,0,1], [0,1,0], 'ro')
plot(listax0, listay0, 'ro')

#plotagem dos padroes da classe 1
plot(listax1, listay1, 'g^')

show()


