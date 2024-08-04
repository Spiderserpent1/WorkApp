from math import e
import ttkbootstrap as ttk 
from Socket_TCP import Connector
import tkinter as tk



#Loads the time changing window
class Parameterwindow(ttk.Toplevel,Connector): 
    def __init__(self, parent): 
        super().__init__(parent,Connector)
        self.parent = parent
        self.connect = Connector
        
        self.title("Parmaeter Selection")
        self.geometry("600x400")

        #establish the frame, scrollbar with prompt, and the window
        self.frame = ttk.Frame(self)
        self.frame.pack()
       
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(side = "bottom", fill = "x", expand = True)
        
        self.time = ttk.Scrollbar(self.frame, orient = "horizontal",command = self.time_change)
        self.time.pack(side = "bottom", fill = "x")
        
        self.prompt = ttk.Label(self.frame, text = "Please enter the time: \n")
        self.prompt.pack(side = "top",fill = 'both', expand = True)
        
        self.canvas.configure(yscrollcommand=self.time.set)


        self.content_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        self.entry_var = tk.StringVar()

# Create an Entry widget linked to the StringVar
        self.entry = ttk.Entry(self.frame, textvariable=self.entry_var, width=30)
        self.entry.pack(pady=10)
        

# Add some content to the content_frame (for demonstration)
        #for i in range(50):
            #ttk.Label(self.content_frame, text=f"{i + 1} minutes").pack()
    

        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)


# Update the canvas scroll region when the content changes
        self.content_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        self.parent.done[1] = True
        print(parent.done)
    

#Runs the time change scrollbar
    def time_change(self,*args):
        self.canvas.yview(*args)
        self.entry_var.set(f"Time set to {49 * (self.time.get()[0] + 1)} minutes")

    def on_mouse_wheel(self, event):
       
       # Determine the scroll direction
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        else:
            self.canvas.yview_scroll(1, "units")
       
        # Update the scrollbar and Entry widget
        self.time.set(*self.canvas.yview())
        self.entry_var.set(f"Time set to {int(49 * (self.time.get()[0]) + 1)} minutes")
        

#Register the waveform to be selected
class Waveformwindow(ttk.Toplevel,Connector):
    def __init__(self, parent): 
        super().__init__(parent,Connector)
        self.parent = parent
        self.connect = Connector
        self.title("Waveform Window")
        self.geometry("250x200")
                
      #Runs the waveform window with prompt
        self.lframe = ttk.Frame(self)
        self.lframe.pack(side = "top",fill = "both",pady = 50)

        self.frame = ttk.Frame(self)
        self.frame.pack(side = "top", pady = 20, fill = "both")
        
        self.choice = ttk.Button(self.frame, text = "Ramping", command = self.ramping) 
        self.choice.pack(side = 'left', fill = 'x', expand = True, padx = 5)
        
        self.choice2 = ttk.Button(self.frame, text = "Sinusoid", command = self.ramping) 
        self.choice2.pack(side = 'left', fill = 'x', expand = True,padx = 5)
        
        self.prompt = ttk.Label(self.lframe, text = "Please select an option for your voltage shape.").pack()
        
        self.parent.done[0] = True
        print(self.parent.done)



#On selection of either choice, runs the ramping function
    def ramping(self): 
        
        Parameterwindow(self)
        self.time = ttk.Scrollbar(self,)
       
        self.connect.algorithm(self)
        


#Select whether or not you want to get the dataset
class Datawindow(ttk.Toplevel): 
    def __init__(self, parent): 
        super().__init__(parent)
        self.parent = parent
        
        self.title("Datawindow")
        self.geometry("600x400")
        
        self.parent.done[2] = True
        print(parent.done)



#Probably will be deprecated
class Analyzer_window(ttk.Toplevel): 
    def __init__(self,parent): 
        super().__init__(parent) 
        self.parent = parent
        
        self.parent.selected = True
        self.title("Voltage Analyzer")
        self.geometry("600x400")