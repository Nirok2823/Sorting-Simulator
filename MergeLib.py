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

class MergeSort:
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
        
    
    def merge(self,lista, izq, der):
        i = j = k = 0
        
        while i < len(izq) and j < len(der):
            self.steps+=1
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i+=1
            else:
                lista[k] = der[j]
                j+=1;
            k+=1
            
        while i < len(izq):
            self.steps+=1
            lista[k] = izq[i]
            i+=1
            k+=1
            
        while j < len(der):
            self.steps+=1
            lista[k] = der[j]
            j+=1
            k+=1

    def mergeSort(self,lista):
        self.steps+=1
        if len(lista) > 1:
            mid = len(lista)//2
            izq = lista[:mid] #todo lo que esta a la izquierda (todos los anteriores) hasta mid
            der = lista[mid:] #e igualmente que alterior, pero desde mid hatsa todo lo anterior
            
            self.mergeSort(izq)
            self.mergeSort(der)
            
            self.merge(lista, izq, der) #enviara la sublista
    
    
    def mergeAnime(self,lista, izq, der):
        i = j = k = 0
        
        while i < len(izq) and j < len(der):
            if not self.running:
                return
            self.steps+=1
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i+=1
            else:
                lista[k] = der[j]
                j+=1;
            self.graph(lista)
            self.master.update()
            time.sleep(self.speed)
            k+=1
            
        while i < len(izq):
            if not self.running:
                return
            self.steps+=1
            lista[k] = izq[i]
            i+=1
            k+=1
            self.graph(lista)
            self.master.update()
            time.sleep(self.speed)
            
        while j < len(der):
            if not self.running:
                return
            self.steps+=1
            lista[k] = der[j]
            j+=1
            k+=1
            self.graph(lista)
            self.master.update()
            time.sleep(self.speed)

    def mergeSortAnime(self,lista):
        if len(lista) > 1:
            mid = len(lista)//2
            izq = lista[:mid] #todo lo que esta a la izquierda (todos los anteriores) hasta mid
            der = lista[mid:] #e igualmente que alterior, pero desde mid hatsa todo lo anterior
            
            if not self.running:
                return
            self.graph(lista)
            self.master.update()
            time.sleep(self.speed)
            self.mergeSortAnime(izq)
            self.mergeSortAnime(der)
            
            self.mergeAnime(lista, izq, der)
                    
    def Merge(self):
        self.mergeSort(self.lista)
        
    def MergAnimation(self):
        self.mergeSortAnime(self.lista)
                    
    def startAnime(self):
        self.running = True
        self.MergAnimation()

    def stopAnime(self):
        self.running = False
                
        
        
    def graph(self,lista):
        self.canvas.delete("all")
        width = 1200
        height = 400
        
        bar_width = width / len(lista)
        max_val = max(lista)
        if(max_val != 0):
            for i, value in enumerate(lista):
                x0 = i * bar_width
                y0 = height
                x1 = (i + 1) * bar_width
                y1 = height - (value / max_val * height)
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")
        
            
        
                
       
                    
class MergeApp:
    def __init__(self, master,canvas, speed):
        self.obj = MergeSort(master,canvas,speed)
        #self.obj.insertSample(lista)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.Merge()
        self.obj.time = time.time() - auxTime
        
        
    def getSteps(self):
        return self.obj.steps
    
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "Merge Sort \t\t n log(n) \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
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