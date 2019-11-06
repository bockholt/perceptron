#!/usr/bin/env python
# Name: Perceptron.py
# Purpose: Classe que implementa o classficador Perceptron
# Author: Tiago Bockholt <tiagobockholt@gmail.com>


class Perceptron:
    """ Classe para implementar o Perceptron"""
    
    def __init__(self, pesos, data, dclasse, n):
        
        self.pesos = pesos
        self.data = data       
        self.dclasse = dclasse
        self.n= n
        self.alfa=0
        self.beta=0
        
    def treinaPerceptron(self):
        erro_global=1
        
        while erro_global!=0:
               
                    
            erro_global, erro_lista = self.calculaErroGlobal()
            #print erro_global, erro_lista
            if erro_global == 0:
                 
                return self.getAlfaBeta()
                        
            else:
                # para cada padrao do conjunto de treinamento
                for i in range(len(self.data)):
                    
                    pesos = self.ajustaPesos(erro_lista[i], self.data[i])
                print self.getAlfaBeta()
            
    
    def getAlfaBeta(self):
        #vai retornar a classe achado pelo perceptron
        
        alfa = - ( self.pesos[1]/self.pesos[2])
        beta = self.pesos[0]/self.pesos[2]
        
        
        y= "y = "+str(-(self.pesos[1]/self.pesos[2])) +"x +"+ str((self.pesos[0]/self.pesos[2]))
        
        return alfa, beta
    
    def calculaClasse(self,padrao):
          
        saida=0
        temp=0 
        
        for  i in range(len(self.pesos)):
                   
            temp=self.pesos[i]*padrao[i]        
            saida=temp+saida
            
        if saida < 0:
            
            classe=0
        else:
            classe=1
            
        return classe
    
    def calculaErroGlobal(self):
        
        yclasse = []
        
        #calcula a classe de saida de cada padrao e insere numa lista (padrao, peso associado a cada padrao)
        for padrao in self.data:
            yclasse.append(self.calculaClasse(padrao))
        
        erro_lista=[0,0,0,0]
        
        
        for i in range(len(yclasse)):
            
            erro_lista[i]= self.dclasse[i] - yclasse[i]
            
        erro_global = sum(erro_lista)
        return erro_global, erro_lista
            
    def ajustaPesos(self, erro_padrao, padrao):
        
        for i in range(len(self.pesos)):
            
           self.pesos[i] = self.pesos[i] + self.n*erro_padrao*padrao[i]       
        
        return self.pesos  
       


       
    
    
    
