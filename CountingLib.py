# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:22:31 2024

@author: Dell
"""

import random
import time

class CountingSort:
    def __init__(self,master,canvas, speed):
        self.master = master
        self.canvas = canvas
        self.lista = []
        self.steps=0;
        self.time = 0
        self.running = False
        if speed == 20:
            self.speed = 1;
        elif speed == 40:
            self.speed = 0.5
            
        elif speed == 60:
            self.speed = 0.1
        elif speed == 80:
            self.speed = 0.03
        elif speed == 100:
            self.speed = 0.001
        
    def insert(self,valor):
        self.lista.append(valor);
        
    def insertSample(self,lista):
        self.lista = []
        self.steps = 0
        self.time = 0
        for i in lista:
            self.lista.append(i);
        
    def insertFullSample(self, minimo, maximo):
        self.lista = random.sample(range(minimo, maximo), maximo-minimo);
        
    def show(self):
        for i in self.lista:
            print(i, end=" ")
        print()
    
    def Counting(self):
        leng = len(self.lista);
        maxi=max(self.lista);     
        #Se define el maximo de la lista
        lista_conteo = [0]*(maxi+1)
        
        for i in self.lista:
            lista_conteo[i]+=1
            self.steps+=1
        
        for i in range(1,len(lista_conteo)):
            lista_conteo[i]+=lista_conteo[i-1];
            self.steps+=1
            
        lista_salida=[0]*leng
        
        for i in self.lista:
            lista_salida[lista_conteo[i]-1]= i
            lista_conteo[i]-=1
            self.steps+=1
        auxSteps = self.steps
        self.insertSample(lista_salida)
        self.steps = auxSteps
        
    def CountingAnimation(self):
        leng = len(self.lista);
        maxi=max(self.lista);     
        #Se define el maximo de la lista
        lista_conteo = [0]*(maxi+1)
        
        for i in self.lista:
            if not self.running:
                return
            lista_conteo[i]+=1
            self.steps+=1
        
        for i in range(1,len(lista_conteo)):
            if not self.running:
                return
            lista_conteo[i]+=lista_conteo[i-1];
            self.steps+=1
            
        lista_salida=[0]*leng
        
        for i in self.lista:
            if not self.running:
                return
            lista_salida[lista_conteo[i]-1]= i
            lista_conteo[i]-=1
            self.steps+=1
            
        #auxSteps = self.steps
        #self.insertSample(lista_salida)
        for i in range(len(lista_salida)):
            if not self.running:
                return
            self.lista[i] = lista_salida[i]
            self.graph()
            self.master.update()
            time.sleep(self.speed)
        #self.steps = auxSteps
        
        
    def startAnime(self):
        self.running = True
        self.CountingAnimation()

    def stopAnime(self):
        self.running = False
                
        
        
    def graph(self):
        self.canvas.delete("all")
        width = 1200
        height = 400
        bar_width = width / len(self.lista)
        max_val = max(self.lista)
        for i, value in enumerate(self.lista):
            x0 = i * bar_width
            y0 = height
            x1 = (i + 1) * bar_width
            y1 = height - (value / max_val * height)
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")
        
class CountingApp:
    def __init__(self, master,canvas, speed):
        self.obj = CountingSort(master,canvas,speed)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.Counting()
        auxTime2 =time.time()
        self.obj.time = auxTime2 - auxTime
        
        
    def getSteps(self):
        return self.obj.steps
    
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "Counting Sort \t\t n+k \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
        return auxTxt
    
    def anime(self):
        self.obj.startAnime()
    
    def Stop(self):
        self.obj.stopAnime()
        
    def addList(self,lista):
        self.obj.lista = lista
    
    def Speed(self,speed):
       if speed == 20:
           self.obj.speed = 1;
       elif speed == 40:
           self.obj.speed = 0.5
           
       elif speed == 60:
           self.obj.speed = 0.1
       elif speed == 80:
           self.obj.speed = 0.03
       elif speed == 100:
          self.obj.speed = 0.001