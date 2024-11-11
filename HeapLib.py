# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:38:02 2024

@author: Dell
"""
import random
import time

class HeapSort:
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
            self.speed = 0.01
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
        
    def heapify(self,lista, n, i):
        hIzq= 2*i+1
        hDer = 2*i+2
        
        if hIzq < n and lista[i] < lista[hIzq]:
            mayor = hIzq
            
        else:
            mayor = i
            
            
        if hDer < n and lista[mayor] < lista[hDer]:
            mayor = hDer
            
            
        if mayor != i:
            lista[i] , lista[mayor] = lista[mayor], lista[i]
            self.steps+=1
            self.heapify(lista, n, mayor)

    def HeapSort(self,lista):
        n = len(lista)
        
        
        for i in range(n//2-1 , -1, -1):
            self.heapify(lista,n,i)
            
        for i in range(n-1, 0, -1):
            lista[0] , lista[i] = lista[i], lista[0]
            self.heapify(lista, i, 0)
            
            
            
    def heapifyAnime(self,lista, n, i):
        hIzq= 2*i+1
        hDer = 2*i+2
        
        if hIzq < n and lista[i] < lista[hIzq]:
            mayor = hIzq
            self.steps+=1
            
        else:
            mayor = i
            self.steps+=1
            
            
        if hDer < n and lista[mayor] < lista[hDer]:
            mayor = hDer
            self.steps+=1
            
            
        if mayor != i:
            if not self.running:
                return
            lista[i] , lista[mayor] = lista[mayor], lista[i]
            self.steps+=1
            self.graph()
            self.master.update()
            time.sleep(self.speed)
            self.heapifyAnime(lista, n, mayor)

    def HeapSortAnime(self,lista):
        n = len(lista)
        self.steps+=1
        
        for i in range(n//2-1 , -1, -1):
            if not self.running:
                return
            self.heapifyAnime(lista,n,i)
            
        for i in range(n-1, 0, -1):
            if not self.running:
                return
            lista[0] , lista[i] = lista[i], lista[0]
            self.heapifyAnime(lista, i, 0)
    
    
    
    def HeapHeap(self):
        self.HeapSort(self.lista)
         
    def HeapAnimation(self):
        self.HeapSortAnime(self.lista)
        
    def startAnime(self):
        self.running = True
        self.HeapAnimation()

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
            

class HeapApp:
    def __init__(self, master,canvas, speed):
        self.obj = HeapSort(master,canvas,speed)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.HeapHeap()
        self.obj.time = time.time() - auxTime
        
    def getSteps(self):
        return self.obj.steps
    
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "Heapl Sort \t\t n(log(n)) \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
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