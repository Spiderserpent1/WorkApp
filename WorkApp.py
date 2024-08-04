import tkinter as tk
import matplotlib as plt
import time
import pandas as pd 
import threading 
import customtkinter as ctk
import ttkbootstrap as ttk
import ttkbootstrap.tooltip as ToolTip
import socket
import ttkcreator

from MainMenu import Voltagewindow 
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Socket_TCP import Connector


#root main code        
class main(ttk.Window): 

    def __init__(self): 
        super().__init__(themename = "litera")
    
        #window configs 
        self.title("Power Supply Toolbox") 
        self.geometry("600x400")
        
        #buttons
        self.voltage_read = ttk.Button(self, text = "Welcome", command = self.open_Vwindow, bootstyle = "primary" )
        self.voltage_read.pack(side = tk.LEFT, expand = True, fill = "x" )
        
        #handler entities
        self.is_reading = False
        self.voltage = []
        self.time = [] 

    #Methods which will probably be deprecated
    def read (self): 
        self.is_reading = True
        self.read_thread = threading.Thread(target = self.practice_reading)
        self.read_thread.start()
        
    def practice_reading(self,Connector):     
        i = 0 
        t = 0 
        while self.is_reading:
            i += 1 * 2 
            t += 1
            Connector.voltage.append(i)
            self.time.append(t) 
            time.sleep(5)
            print(i)
    
    def stop(self): 
        self.is_reading = False
        self.read_thread.join()
        if self.is_reading == False: 
            self.voltage = 5
            df = pd.DataFrame(Connector.voltage, columns = ["Voltage"])
            print(df)
    

    def open_Vwindow(self):
        Voltagewindow(self)
        
    
app = main()
app.mainloop()


