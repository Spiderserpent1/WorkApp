import ttkbootstrap as ttk
import tkinter as tk
import matplotlib.pyplot as plt
import customtkinter as ctk 
from Parameters import   Waveformwindow, Parameterwindow
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.animation import FuncAnimation
import numpy as np 
from Socket_TCP import Connector
import time
import math
#matplotlib plot 




#main menu
class Voltagewindow(ttk.Toplevel):  
    
    def __init__(self,parent): 
        super().__init__(parent)
        self.title("AVR Configuration")
        self.geometry("800x500")
        self.parent = parent
        self.time = 60
        self.x = []
        self.y = []
        self.fig,self.ax = plt.subplots(figsize  = (5,5))        
#Initialize the Frames        
        self.frame1 = ttk.Frame(self, borderwidth = 3, relief = 'ridge')
        self.frame1.place(x = 25, y = 50, width = 200, height = 270)
        
        #self.frame2 = ttk.Frame(self, borderwidth = 3, relief = "ridge")
        #self.frame2.place(x = 250, y = 50, relwidth = .65, relheight = .7)

        self.frame3 = ttk.Frame(self, borderwidth = 3, relief = "ridge")
        self.frame3.place(x = 250, y = 50, relwidth = .65, relheight = .7)

        
        
#define the parameters that the user will set
        self.selectionpane = ttk.Label(self.frame1, text = "Configuration Menu").pack()
        
        self.waveform = ttk.Button(self.frame1, text = "Waveform", command = self.open_waveformwindow, bootstyle = "primary")
        self.waveform.pack(side = tk.TOP,expand = True, pady = 5 )
        
        #self.parameters = ttk.Button(self.frame1, text = "Parameters", command = self.open_parameterwindow, bootstyle = "primary")
        #self.parameters.pack(side = tk.TOP, expand = True,pady = 5)
        
       
        
        self.begin = ttk.Button(self.frame1, text = "Begin", command = self.animate, bootstyle = "primary")
        self.begin.pack(side = tk.TOP, expand = True,pady = 5) 
        
        self.AC_connect = ttk.Label(self.frame3, text = "AC/DC").pack(side = "top")
        self.canvas = FigureCanvasTkAgg(self.fig, master = self.frame3)
        self.canvas.get_tk_widget().pack(side = "bottom")
        
#define the region for the matplotlib graph        
        #self.idletitle = ttk.Label(self.frame2, text = "Realtime Plot")
        #self.idletitle.pack()
        
        #self.frame_box = ttk.Frame(self.frame2, bootstyle = "light",relief = 'ridge', borderwidth = 1)
        #self.frame_box.place(x= 50, y = 50, relwidth = 0.8, relheight = 0.8)                       
        
        self.selected = False        
        self.third_window = False
        self.done = [False,False,False]

#inialize the window
    def open_waveformwindow(self):
        if self.third_window is False:            
            Waveformwindow(self)
        
    def open_parameterwindow(self): 
        Parameterwindow(self)
    
   
    
    def updater(self,frame, *args): 

        self.y.append(math.sin(frame))
        self.x.append(frame)
        self.ax.plot(self.x, self.y)
         
            
    def animate (self):
        self.animation = FuncAnimation(self.fig, self.updater, interval = 1000,frames = range(self.time), cache_frame_data=False) 
        self.canvas.draw()

    def error_handler(self): 
        if self.done != [True,True,True] and self.selected: 
            Errorwindow(self)


#Error Handler
class Errorwindow(ttk.Toplevel): 
    def __init__(self,parent): 
        super().__init__(parent) 
        self.parent = parent
        
        
        self.title("Error: Too Hasty")
        self.geometry("250x200")
        
        self.errorlabel = ttk.Label(self, text = "DO NOT SELECT BEGIN WITHOUT FINISHING!")
        self.errorlabel.pack(side = tk.TOP, fill = "both", expand = True)
        self.confirm_button = ttk.Button(self, text = "I understand", command = self.close)
        self.confirm_button.pack(side = tk.TOP)
        

    def close(self): 
        self.destroy


