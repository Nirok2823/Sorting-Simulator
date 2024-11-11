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

class TimSort:
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
        
    
    def insertion_sort(self,arr, start, end):
        steps = 0
        for i in range(start + 1, end + 1):
            key = arr[i]
            j = i - 1
            steps = 0
            while j >= start and arr[j] > key:
                steps+=1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            if steps != 0:
                self.steps += steps
            else: self.steps+=1

    def merge(self,arr, left, mid, right):
        if mid == 0 or mid >= (len(arr)):
            return
        if arr[mid - 1] <= arr[mid]:
            return

        i, j, k = left, mid, 0
        temp = [0] * (right - left)

        while i < mid and j < right:
            self.steps+=1
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

        while i < mid:
            self.steps+=1
            temp[k] = arr[i]
            i += 1
            k += 1

        while j < right:
            self.steps+=1
            temp[k] = arr[j]
            j += 1
            k += 1

        for i in range(right - left):
            arr[left + i] = temp[i]

    def Tim(self):
        n = len(self.lista)
        min_run = 32

        for i in range(0, n, min_run):
            self.insertion_sort(self.lista, i, min((i + min_run - 1), n - 1))

        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = start + size
                right = min((start + size * 2), n)
                self.merge(self.lista, start, mid, right)
            size *= 2
            
            
    def insertionAnime(self,arr, start, end):
        for i in range(start + 1, end + 1):
            if not self.running:
                return
            key = arr[i]
            j = i - 1
            while j >= start and arr[j] > key:
                if not self.running:
                    return
                arr[j + 1] = arr[j]
                j -= 1
                
            arr[j + 1] = key
            self.graph()
            self.master.update()
            time.sleep(self.speed)
            

    def mergeAnime(self,arr, left, mid, right):
        if mid == 0 or mid >= (len(arr)):
            return
        if arr[mid - 1] <= arr[mid]:
            return

        i, j, k = left, mid, 0
        temp = [0] * (right - left)

        while i < mid and j < right:
            if not self.running:
                return
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            
            k += 1

        while i < mid:
            if not self.running:
                return
            temp[k] = arr[i]
            i += 1
            k += 1

        while j < right:
            if not self.running:
                return
            temp[k] = arr[j]
            j += 1
            k += 1

        for i in range(right - left):
            if not self.running:
                return
            arr[left + i] = temp[i]
            self.graph()
            self.master.update()
            time.sleep(self.speed)
            
            
    def TimAnimation(self):
        n = len(self.lista)
        min_run = 32

        for i in range(0, n, min_run):
            self.insertionAnime(self.lista, i, min((i + min_run - 1), n - 1))

        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = start + size
                right = min((start + size * 2), n)
                self.mergeAnime(self.lista, start, mid, right)
            size *= 2
            
                    
                    
    def startAnime(self):
        self.running = True
        self.TimAnimation()

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
            
        
                
       
                    
class TimApp:
    def __init__(self, master,canvas, speed):
        self.obj = TimSort(master,canvas,speed)
        #self.obj.insertSample(lista)
        
        
    def Show(self):
        self.obj.show()
    
    def Sort(self):
        auxTime = time.time()
        self.obj.Tim()
        self.obj.time = time.time() - auxTime
        
        
    def getSteps(self):
        return self.obj.steps
    
    def Insert(self, lista):
        self.obj.insertSample(lista)
        
    def getTime(self):
        auxTxt = "Tim Sort \t\t nlog(n) \t\t "+ str(self.obj.time)+ "seg \t\t\t\t "+str(self.getSteps())+"\n"
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