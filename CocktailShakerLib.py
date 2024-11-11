# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:38:02 2024

@author: Dell
"""

import random
import time

class CocktailSort:
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
        
    
    def Cocktail(self):
        n = len(self.lista)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            # Reset the swapped flag
            swapped = False

            # Perform a bubble sort from left to right
            for i in range(start, end):
                self.steps += 1
                if self.lista[i] > self.lista[i + 1]:
                    self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]
                    swapped = True

            # If no elements were swapped, the array is sorted
            if not swapped:
                break

            # Update the end index since the largest element is at the end
            end -= 1

            # Perform a bubble sort from right to left
            for i in range(end - 1, start - 1, -1):
                self.steps += 1
                if self.lista[i] > self.lista[i + 1]:
                    self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]
                    swapped = True

            # Update the start index since the smallest element is at the start
            start += 1
            
    def CocktailAnimation(self):
        n = len(self.lista)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            # Reset the swapped flag
            swapped = False

            # Perform a bubble sort from left to right
            for i in range(start, end):
                if not self.running:
                    return
                if self.lista[i] > self.lista[i + 1]:
                    self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]
                    swapped = True
                    self.graph()
                    self.master.update()
                    time.sleep(self.speed)

            # If no elements were swapped, the array is sorted
            if not swapped:
                break

            # Update the end index since the largest element is at the end
            end -= 1

            # Perform a bubble sort from right to left
            for i in range(end - 1, start - 1, -1):
                if not self.running:
                    return
                if self.lista[i] > self.lista[i + 1]:
                    self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]
                    swapped = True
                    self.graph()
                    self.master.update()
                    time.sleep(self.speed)

            # Update the start index since the smallest element is at the start
            start += 1
            
    
                    
                    
    def startAnime(self):
        self.running = True
        self.CocktailAnimation()

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
            
        
                
       
                    
class CocktailApp:
    def __init__(self, master,canvas, speed):
        self.obj = CocktailSort(master,canvas,speed)
        #self.obj.insertSample(lista)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.Cocktail()
        self.obj.time = time.time() - auxTime
        
        
    def getSteps(self):
        return self.obj.steps
    
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "CocktailShaker \t\t n^2 \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
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