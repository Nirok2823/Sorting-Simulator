
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:38:02 2024

@author: Dell
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import customtkinter
import random
import time

class RadixSort:
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
        
    
    def countingB10(self,lista, exp):
        listaCont = 10*[0]
        
        
        for i in lista:
            aux = i // exp
            listaCont[aux % 10] += 1;
            self.steps+=1
            
        for i in range(1, len(listaCont)):
            listaCont[i] += listaCont[i-1]
            self.steps+=1
            
        listaS = len(lista)*[0]
            
        for i in range(len(lista)-1, -1, -1):
            index = (lista[i]//exp) % 10
            auxInd = listaCont[index]-1
            listaCont[index] -= 1
            
            listaS[auxInd] = lista[i]
            self.steps+=1
            
        for i in range(len(listaS)):
            lista[i] = listaS[i]
            self.steps+=1
        


    def radixSort(self,lista):
        maximo = max(lista)
        #print (maximo)
        
        exp = 1
        
        while maximo // exp > 0:
            self.countingB10(lista, exp)
            #print(lista)
            exp *= 10
        
            
    
    def countingB10Anime(self,lista, exp):
        listaCont = 10*[0]
        
        
        for i in lista:
            if not self.running:
                return
            aux = i // exp
            listaCont[aux % 10] += 1;
            self.steps+=1
            
        for i in range(1, len(listaCont)):
            if not self.running:
                return
            listaCont[i] += listaCont[i-1]
            self.steps+=1
            
        listaS = len(lista)*[0]
            
        for i in range(len(lista)-1, -1, -1):
            if not self.running:
                return
            index = (lista[i]//exp) % 10
            auxInd = listaCont[index]-1
            listaCont[index] -= 1
            
            listaS[auxInd] = lista[i]
            self.steps+=1
            
        for i in range(len(listaS)):
            if not self.running:
                return
            lista[i] = listaS[i]
            self.steps+=1
            self.graph()
            self.master.update()
            time.sleep(self.speed)
        


    def radixSortAnime(self,lista):
        maximo = max(lista)
        #print (maximo)
        
        exp = 1
        
        while maximo // exp > 0:
            if not self.running:
                return
            self.countingB10Anime(lista, exp)
            #print(lista)
            exp *= 10
            
    
    def RadixS(self):
        self.radixSort(self.lista)
        
    def RadixAnimation(self):
        self.radixSortAnime(self.lista)
                    
                    
    def startAnime(self):
        self.running = True
        self.RadixAnimation()

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
            
        
                
       
                    
class RadixApp:
    def __init__(self, master,canvas, speed):
        self.obj = RadixSort(master,canvas,speed)
        #self.obj.insertSample(lista)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.RadixS()
        self.obj.time = time.time() - auxTime
        
        
    def getSteps(self):
        return self.obj.steps
    
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "Radix Sort \t\t d(n+k) \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
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