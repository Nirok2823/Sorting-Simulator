# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:38:02 2024

@author: Dell
"""

import random
import time

class QuickSort:
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
        
    
    def partition(self, izq, der, pivote):
        i = izq -1
        
        for j in range(izq,der):
            self.steps+=1
            if self.lista[j] < pivote:
                i += 1
                self.lista[i] , self.lista[j] = self.lista[j], self.lista[i];
                
        i+=1
        self.lista[i], self.lista[der] = self.lista[der], self.lista[i]
        return i 
        
    def quickSort(self, izq, der):
        if izq >= der:
            return
        else:
            pivote = self.lista[der]
            particion = self.partition(izq, der, pivote)
            self.quickSort(izq, particion-1)
            self.quickSort(particion+1, der)
            
            
    
            
    def partitionAnime(self, izq, der, pivote):
        i = izq -1
        
        for j in range(izq,der):
            if not self.running:
                return
            self.steps+=1
            if self.lista[j] < pivote:
                i += 1
                self.lista[i] , self.lista[j] = self.lista[j], self.lista[i];
                self.graph()
                self.master.update()
                time.sleep(self.speed)
                
        i+=1
        self.lista[i], self.lista[der] = self.lista[der], self.lista[i]
        self.graph()
        self.master.update()
        time.sleep(self.speed)
        return i 
        
    def quickSortAnime(self, izq, der):
        if izq >= der:
            return
        else:
            if not self.running:
                return
            pivote = self.lista[der]
            particion = self.partitionAnime(izq, der, pivote)
            self.quickSortAnime(izq, particion-1)
            self.quickSortAnime(particion+1, der)
            
    def to_quickSort(self):
        self.quickSort(0, len(self.lista)-1)
        
    def QuickAnimation(self):
        self.quickSortAnime(0, len(self.lista)-1)
                                  
    def startAnime(self):
        self.running = True
        self.QuickAnimation()

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
            
        
                
       
                    
class QuickApp:
    def __init__(self, master,canvas, speed):
        self.obj = QuickSort(master,canvas,speed)
        #self.obj.insertSample(lista)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.to_quickSort()
        self.obj.time = time.time() - auxTime
        
        
    def getSteps(self):
        return self.obj.steps
    
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "Quick Sort \t\t n log(n) \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
        return auxTxt
    def getTime2(self):
        auxTxt = "Quick Sort \t\t n^2 \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
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