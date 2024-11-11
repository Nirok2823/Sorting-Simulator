# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:38:02 2024

@author: Dell
"""
import random
import time

class InsertionSort:
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
        
    #Insertion Sort
    def Insertion(self):
        long=len(self.lista);
        steps = 0
        
        for i in range(1,long):
            temp=self.lista[i];
            steps = 0
            j=i
            
            while( j > 0 and self.lista[j - 1]>temp):
                steps+=1
                self.lista[j] = self.lista[j-1];
                j -= 1;
                
            self.lista[j]=temp;
            if steps != 0:
                self.steps += steps
            else: self.steps+=1
           
                
            
    def getSteps(self):
        return self.steps
    
    
    def InsertionAnimation(self):
        long=len(self.lista);
        steps = 0
        
        for i in range(1,long):
            if not self.running:
                return
            temp=self.lista[i];
            steps = 0
            j=i
            
            while( j > 0 and self.lista[j - 1]>temp):
                if not self.running:
                    return
                steps+=1
                self.lista[j] = self.lista[j-1];
                j -= 1;
                self.graph()
                self.master.update()
                time.sleep(self.speed)
                
                
            self.lista[j]=temp;
            self.graph()
            self.master.update()
            time.sleep(self.speed)
            if steps != 0:
                self.steps += steps
            else: self.steps+=1
            
    def startAnime(self):
        self.running = True
        self.InsertionAnimation()

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
        

class InsertionApp:
    def __init__(self, master,canvas, speed):
        self.obj = InsertionSort(master,canvas,speed)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.Insertion()
        self.obj.time = time.time() - auxTime
        
        
        
    def getSteps(self):
        return self.obj.getSteps()
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "Insertion Sort \t\t n^2 \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
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
           self.obj.speed = 0.05
       elif speed == 100:
          self.obj.speed = 0.001


    