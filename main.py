# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:04:10 2024

@author: Dell
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import customtkinter
import random
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkFrame, CTkRadioButton, CTkTextbox, CTkFont
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
from SelectionLib import SelectApp
from InsertionLib import InsertionApp
from BubbleLib import BubbleApp
from ShellLib import ShellApp
from CountingLib import CountingApp
from HeapLib import HeapApp
from QuickLib import QuickApp
from MergeLib import MergeApp
from RadixLib import RadixApp
from TimSort import TimApp
from CocktailShakerLib import CocktailApp
import time
import tkinter as tk
from matplotlib.figure import Figure

toplevel_window = None
#Ventana Secundaria
class ToplevelWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Testing Sorts")
        self.geometry(f"{1200}x{600}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Sidebar Frame
        self.sidebar_frame = CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        # Logo
        self.logo_label = CTkLabel(self.sidebar_frame, text="TEST", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Sidebar Buttons
        self.sidebar_button_1 = CTkButton(self.sidebar_frame, text="INICIO", command=self.sortOp)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = CTkButton(self.sidebar_frame, text="CERRAR", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
       
        self.orderCheck = customtkinter.IntVar(value=None)
         
        # Radio buttons
        self.radiobutton_frame = CTkFrame(self,width=50)
        self.radiobutton_frame.grid(row=0, column=3, padx=(10, 10), pady=(30, 30), sticky="nw")
        self.radio_var = customtkinter.IntVar(value=0)
        self.label_radio_group = CTkLabel(master=self.radiobutton_frame, text="Método de ordenamiento")
        self.label_radio_group.grid(row=0, column=0, padx=9, pady=10, sticky="ew")
        self.radio_button_1 = CTkRadioButton(master=self.radiobutton_frame, text="RANDOM", variable=self.orderCheck, value=1)
        self.radio_button_1.grid(row=1, column=0, padx=9, pady=10, sticky="ew")
        self.radio_button_2 = CTkRadioButton(master=self.radiobutton_frame, text="INVORD", variable=self.orderCheck, value=2)
        self.radio_button_2.grid(row=2, column=0, padx=9, pady=20, sticky="ew")
        
       
        # Caja de texto
        self.textbox = CTkTextbox(self, width=50)
        self.textbox.grid(row=0, column=1, padx=(10, 10), pady=(20, 20), sticky="new")
        
        self.txtBox = CTkTextbox(self, width=50, height=15)
        self.txtBox.grid(row=0, column=1, padx=(10, 10), pady=(20, 20), sticky="nsew")

        #GRAFICA
        self.fig = Figure(figsize=(6, 6))  # Ancho de 6 pulgadas, alto de 4 pulgadas
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122)
        self.ax1.set_xlabel('Items')
        self.ax1.set_ylabel('Iteraciones')
        self.ax1.set_title('n^2')
        self.ax2.set_xlabel('Items')
        self.ax2.set_ylabel('Iteraciones')
        self.ax2.set_title('n+k y nlog(n)')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=1, padx=(20, 10), pady=(20, 20), sticky="sew")

    def sidebar_button_event(self):
        print("Cerrando la aplicación...")
        self.destroy()

    def sortOp(self):
    
        op = self.orderCheck.get()
        lista= []
        if op == 1:
            lista = random.sample(range(0, 2000), 2000);
        elif op == 2:
            for i in range(2000,-1, -1):
                lista.append(i)
    
        if op is not None: 
            self.Graficar(lista)

    def Graficar(self, lista):
        self.ax1.clear()
        self.ax2.clear()
        ord1 = BubbleApp(0,0,0)
        ord2 = InsertionApp(0,0,0)
        ord3 = SelectApp(0,0,0)
        ord4 = ShellApp(0,0,0)
        ord5 = CountingApp(0,0,0)
        ord6 = HeapApp(0,0,0)
        ord7 = QuickApp(0,0,0)
        ord8 = MergeApp(0,0,0)
        ord9 = RadixApp(0,0,0)
        ordA = TimApp(0,0,0)
        ordB = CocktailApp(0,0,0)
        
        ord1.Insert(lista)
        ord2.Insert(lista)
        ord3.Insert(lista)
        ord4.Insert(lista)
        ord5.Insert(lista)
        ord6.Insert(lista)
        ord7.Insert(lista)
        ord8.Insert(lista)
        ord9.Insert(lista)
        ordA.Insert(lista)
        ordB.Insert(lista)
    
        ord1.Sort()
        ord2.Sort()
        ord3.Sort()
        ord4.Sort()
        ord5.Sort()
        ord6.Sort()
        ord7.Sort()
        ord8.Sort()
        ord9.Sort()
        ordA.Sort()
        ordB.Sort()
        
        
        auxTxt = "Metodo: \t\t Big O: \t\t Tiempo de ejecucion: \t\t\t\t Iteraciones: \n"
    
        s = []
        it = []
        auxlista = []
        for i in range(11):
            if i == 0:
                
                auxTxt+= ord1.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord1.Insert(auxlista)
                    ord1.Sort()
                    s.append(ord1.getSteps())
                    it.append(i)
                self.ax1.plot(it,s, label = "Bubble") 
                self.ax1.set_xlabel('Items')
                self.ax1.set_ylabel('Iteraciones')
                self.ax1.set_title('n^2')
                self.ax1.legend()
                
                    
            elif i == 1:
                auxTxt+= ord2.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord2.Insert(auxlista)
                    ord2.Sort()
                    s.append(ord2.getSteps())
                    it.append(i)
                self.ax1.plot(it,s,label = "Insertion")
                self.ax1.legend()
            elif i == 2:
                auxTxt+= ord3.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord3.Insert(auxlista)
                    ord3.Sort()
                    s.append(ord3.getSteps())
                    it.append(i)
                self.ax1.plot(it,s,label = "Selection")
                self.ax1.legend()
            elif i == 3:
                auxTxt+= ord4.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord4.Insert(auxlista)
                    ord4.Sort()
                    s.append(ord4.getSteps())
                    it.append(i)
                self.ax2.plot(it,s,label = "Shell")
                self.ax2.set_xlabel('Items')
                self.ax2.set_ylabel('Iteraciones')
                self.ax2.set_title('n+k y nlog(n)')
                self.ax2.legend()
            elif i == 4:
                auxTxt+= ord5.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord5.Insert(auxlista)
                    ord5.Sort()
                    s.append(ord5.getSteps())
                    it.append(i)
                self.ax2.plot(it,s,label = "Counting") 
                self.ax2.legend()
            elif i == 5:
                auxTxt+= ord6.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord6.Insert(auxlista)
                    ord6.Sort()
                    s.append(ord6.getSteps())
                    it.append(i)
                self.ax2.plot(it,s,label = "Heap")
                self.ax2.legend()
                
            elif i == 6:
                if(ord7.getSteps() < 1000000):
                    auxTxt+= ord7.getTime()
                else:auxTxt+= ord7.getTime2()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord7.Insert(auxlista)
                    ord7.Sort()
                    s.append(ord7.getSteps())
                    it.append(i)
                if(s[len(s)-1] < 1000000):
                    self.ax2.plot(it,s, label = "Quick")
                    self.ax2.legend()
                
                else: 
                    self.ax1.plot(it,s, label = "Quick")
                    self.ax1.legend()
                
            elif i == 7:
                auxTxt+= ord8.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord8.Insert(auxlista)
                    ord8.Sort()
                    s.append(ord8.getSteps())
                    it.append(i)
                self.ax2.plot(it,s, label = "Merge")
                self.ax2.legend()
                
            elif i == 8:
                auxTxt+= ord9.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ord9.Insert(auxlista)
                    ord9.Sort()
                    s.append(ord9.getSteps())
                    it.append(i)
                self.ax2.plot(it,s, label = "Radix")
                self.ax2.legend()
                
            elif i == 9:
                auxTxt+= ordA.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ordA.Insert(auxlista)
                    ordA.Sort()
                    s.append(ordA.getSteps())
                    it.append(i)
                self.ax2.plot(it,s, label = "Tim")
                self.ax2.legend()
                
                   
            elif i == 10:
                auxTxt+= ordB.getTime()
                s = []
                it = []
                for i in range(400,2001,+400):
                    auxlista = lista[:i]
                    ordB.Insert(auxlista)
                    ordB.Sort()
                    s.append(ordB.getSteps())
                    it.append(i)
                self.ax1.plot(it,s, label = "Cocktail")
                self.ax1.legend()
    
        #self.ax.bar(meth, s, color=colores)
        self.canvas.draw()
        self.txtBox.delete(0.0, "end")
        self.txtBox.insert(0.0, auxTxt)

lista = []
x = []
auxList = []
i = 0
obj = object()

#Ventana Principal

def graph():
    global lista
    global x
    canvas.delete("all")
    width = 1200
    height = 400
    bar_width = width / len(lista)
    max_val = max(lista)
    for i, value in enumerate(lista):
        x0 = i * bar_width
        y0 = height
        x1 = (i + 1) * bar_width
        y1 = height - (value / max_val * height)
        canvas.create_rectangle(x0, y0, x1, y1, fill="green")
    

def generateNewGraph():
    global lista
    global x
    global auxList
    global i 
    global obj
    obj = None
    auxList = []
    
    i = 0
    n = int(slider_1.get())
    print(n)
    lista = [i for i in random.sample(range((0),n),n)]
    for i in lista:
        auxList.append(i)
    x = [i for i in range(0,n)]
    sList = sorted(lista)
    graph()
    
    
    
def changeSpeed():
    global obj
    obj.Speed(int(slider_2.get()))
    
    
def Play():
    global lista
    global x
    #global sList
    global obj
    global i
    
    
    
    if radio_var.get() == 0:
        obj = BubbleApp(main,canvas, int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 1:
        obj = InsertionApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 2:
        obj = SelectApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 3:
        obj = CountingApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 4:
        obj = ShellApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 5:
        obj = HeapApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 6:
        obj = QuickApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 7:
        obj = MergeApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
    
    elif radio_var.get() == 8:
        obj = RadixApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 9:
        obj = TimApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
        
    elif radio_var.get() == 10:
        obj = CocktailApp(main,canvas,int(slider_2.get()))
        obj.addList(lista)
     
    obj.anime()
    
def Stop():
    global obj
    global lista
    
    obj.Stop()
    
def resetGraph():
    global auxList
    global lista
    
    lista = []
    for i in auxList:
        lista.append(i)
    graph()
    
    
def open_toplevel():
    global toplevel_window
    if toplevel_window is None or not toplevel_window.winfo_exists():
        toplevel_window = ToplevelWindow(main)  
    else:
        toplevel_window.focus()
    
def sliding1(val):
    sliderValue.configure(text = int(val))
    
def sliding2(val):
    sliderValue2.configure(text = int(val))



customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

main = customtkinter.CTk()
main.title("Sort Simulator")
main.grid_columnconfigure(1, weight=1)
main.grid_columnconfigure((2, 3), weight=0)
main.grid_rowconfigure((0, 1, 2), weight=1)
main.geometry(f"{1400}x{500}")


sidebar_frame = customtkinter.CTkFrame(main, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
sidebar_frame.grid_rowconfigure(7, weight=1)

logo_label = customtkinter.CTkLabel(sidebar_frame, text="EXPLORE", font=customtkinter.CTkFont(size=40, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, text="TEST", command=open_toplevel)
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, text="CH SPEED", command=changeSpeed)
sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
sidebar_button_4 = customtkinter.CTkButton(sidebar_frame, text="PLAY", command=Play)
sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)
sidebar_button_5 = customtkinter.CTkButton(sidebar_frame, text="STOP", command=Stop)
sidebar_button_5.grid(row=4, column=0, padx=20, pady=10)
sidebar_button_6 = customtkinter.CTkButton(sidebar_frame, text="RESET", command=resetGraph)
sidebar_button_6.grid(row=5, column=0, padx=20, pady=10) 
sidebar_button_7 = customtkinter.CTkButton(sidebar_frame, text="NEW", command=generateNewGraph)
sidebar_button_7.grid(row=6, column=0, padx=20, pady=10)   


# Slider and Slider Frame
slider_progressbar_frame = customtkinter.CTkFrame(main, fg_color="transparent")
slider_progressbar_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
slider_progressbar_frame.grid_columnconfigure(0, weight=1)
slider_progressbar_frame.grid_rowconfigure(5, weight=1) 


# Slider 1
slider_title_1 = customtkinter.CTkLabel(slider_progressbar_frame, text="Cantidad de valores")
slider_title_1.grid(row=7, column=0, padx=10, pady=(20, 10), sticky="ew")
slider_1 = customtkinter.CTkSlider(slider_progressbar_frame, from_=10, to=1000,number_of_steps=990, command=sliding1, width=200)
slider_1.grid(row=8, column=0, padx=(20, 10), pady=(20, 10), sticky="ew")
left_text_1 = customtkinter.CTkLabel(slider_progressbar_frame, text="10 val")
left_text_1.grid(row=9, column=0, padx=(20, 0), pady=(0, 10), sticky="w")
sliderValue = customtkinter.CTkLabel(slider_progressbar_frame, text= slider_1.get())
sliderValue.grid(row = 9, column = 0, padx=(10, 0), pady=(0, 10), sticky="ew")
right_text_1 = customtkinter.CTkLabel(slider_progressbar_frame, text="1,000 val")
right_text_1.grid(row=9, column=0, padx=(0, 20), pady=(0, 10), sticky="e") 


# Slider 2
slider_title_2 = customtkinter.CTkLabel(slider_progressbar_frame, text="Velocidad %")
slider_title_2.grid(row=7, column=1, padx=10, pady=(20, 10), sticky="ew")
slider_2 = customtkinter.CTkSlider(slider_progressbar_frame, from_=20, to=100, number_of_steps=4,command = sliding2, width=200)
slider_2.grid(row=8, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")
left_text_2 = customtkinter.CTkLabel(slider_progressbar_frame, text="<<<")
left_text_2.grid(row=9, column=1, padx=(20, 0), pady=(0, 0), sticky="w")
sliderValue2 = customtkinter.CTkLabel(slider_progressbar_frame, text= slider_2.get())
sliderValue2.grid(row = 9, column = 1, padx=(10, 0), pady=(0, 10), sticky="nsew")
right_text_2 = customtkinter.CTkLabel(slider_progressbar_frame, text=">>>")
right_text_2.grid(row=9, column=1, padx=(0, 20), pady=(0, 0), sticky="e")

# Radio Buttons
radiobutton_frame = customtkinter.CTkFrame(main, width=140, height = 600)
radiobutton_frame.grid(row=0, column=3, padx=(10, 10), pady=(20, 0), sticky="nsew")
radio_var = customtkinter.IntVar(value=0)
label_radio_group = customtkinter.CTkLabel(master=radiobutton_frame, text="Método de ordenamiento")
label_radio_group.grid(row=0, column=0, padx=9, pady=10, sticky="w")
methods = ["Bubble", "InsertionSort", "SelectionSort", "CountingSort", "ShellSort", "HeapSort", "QuickSort", "MergeSort", "RadixSort", "TimSort",
           "Cocktail Shaker"]
radio_buttons = []

for i, method in enumerate(methods):
    radio_button = customtkinter.CTkRadioButton(master=radiobutton_frame, text=method, variable=radio_var, value=i)
    radio_button.grid(row=i + 1, column=0, pady=5, padx=10, sticky="w")
    radio_buttons.append(radio_button)

        
#GRAFICA
plotFrame = customtkinter.CTkFrame(main, fg_color="transparent", width=1200, height = 400)
plotFrame.grid(row=0, column=1, padx=(0,0), pady=0, sticky = "n")
canvas = customtkinter.CTkCanvas(plotFrame, width=1200, height=400, bg = "black")
canvas.pack()


main.mainloop()