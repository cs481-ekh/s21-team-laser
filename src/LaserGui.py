import rawTAspectrum
import tkinter as tk
from tkinter import ttk
from tkinter import Entry, filedialog, messagebox
from threading import Thread
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter.filedialog import asksaveasfile

import os
from tkinter.ttk import Button

class Project(tk.Frame):
    def __init__(self,parent):
        #initialize GUI variables
        tk.Frame.__init__(self,parent)

        #class variables
        self.tabCount =1
        self.tabPanel = ttk.Notebook(self)
        self.tabPanel.pack(fill="both", expand=True)

        myMenu = tk.Menu(self)
        parent.config(menu=myMenu)

        #add menu Items
        menu1 = tk.Menu(myMenu)
        myMenu.add_cascade(label="File", menu=menu1)
        menu1.add_command(label="Select a file", command=self.open_file)

        # menu1.add_command(label="Save a file", command=self.save_image)

        menu2 = tk.Menu(myMenu)
        myMenu.add_cascade(label="Menu 2", menu=menu2)
        #menu2.add_command(label="Menu Item", command=self.emptyCommand)
        #menu2.add_command(label="Menu Item", command=self.emptyCommand)


    def create_tab(self):
        # created new tabs
        self.tab = tk.Frame(self.tabPanel)
        self.tab.pack(fill="both")
        self.tabPanel.add(self.tab,text="Tab" + str(self.tabCount))
        self.tabCount = self.tabCount+1


    def create_graph1(self):
        # created new tabs
        self.tab = tk.Frame(self.tabPanel)
        self.tab.columnconfigure(0,weight=0)
        self.tab.columnconfigure(3,weight=1)
        self.tab.rowconfigure(0,weight=0)
        #self.tab.pack(fill="both")
        self.tabPanel.add(self.tab,text="Tab" + str(self.tabCount))
        #self.tabCount = self.tabCount+1
        
        self.label1 = tk.Label(self.tab,text="Wlax1")
        self.Wlax1 = tk.Entry(self.tab)
        self.label1.grid(column=0,row=0)
        self.Wlax1.grid(column=1,row=0)

        self.label2 = tk.Label(self.tab,text="Wlax2")
        self.Wlax2 = tk.Entry(self.tab)
        self.label2.grid(column=0,row=1)
        self.Wlax2.grid(column=1,row=1)

        self.label3 = tk.Label(self.tab,text="Taxcp")
        self.taxcp = tk.Entry(self.tab)
        self.label3.grid(column=0,row=2)
        self.taxcp.grid(column=1,row=2)

        btn_apply = Button(self.tab, text="Apply", command=self.tuncate_data)
        btn_apply.grid(column=0,row=3)

        btn_remove = Button(self.tab, text="Remove Tab", command=self.remove_tab)
        btn_remove.grid(column=1,row=3)
        self.graph1 = tk.Frame(self.tab)
        self.graph1.grid(column=2,row=0,rowspan=4,sticky="nsew")

    def apply_button_action(self):
        print(self.entry.get())    

    #opens data file and funs analysis
    def open_file(self):
        self.fileName = filedialog.askopenfilename(initialdir="/C:", title="Select a File", filetypes=(("DAT files", "*.dat"),("All files", "*.*")))
        #rawTAspectrum.load_chart(self.fileName)
        controlThread = Thread(target=self.start_thread, daemon=True)
        controlThread.start()
    
    def get_tab_count(self):
        return self.tabCount
    
    def start_thread(self):
        #variable for progress bar on GUI
        progressBar = ttk.Progressbar(root,orient=tk.HORIZONTAL,length=200,mode="indeterminate",takefocus=True,maximum=100)
        global fig
        progressBar.start()
        progressBar.pack()
        self.update() 
        rawTAspectrum.load_data_file(self.fileName)
        fig = rawTAspectrum.dummy_chart()
        progressBar.stop()
        progressBar.destroy()
        self.after(0,self.draw_plot)
    
    def draw_plot(self):
        self.create_graph1()
        canvas = FigureCanvasTkAgg(fig, master=self.graph1)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.graph1)
        toolbar.update()
        canvas.draw()
        self.update()
        
    def tuncate_data(self):
        #get input text
        wlax1 = self.Wlax1.get()
        wlax2 = self.Wlax2.get()
        taxcp = self.taxcp.get()
        #test for bad input. 
        try:
            float(wlax1)
            print("float value")
        except:
            print("Not float")

    # def save_image(self):
    #     files = [("All files", "*.*" ),
    #             ("Python files", "*.py"),
    #             ("Text document", "*.txt"),
    #             ("Image files", "*.png")]
    #     file = asksaveasfile(filetypes = files, defaultextension = '.png')

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Laser Noise Analysis App')
    root.geometry("1000x700")
    Project(root).pack(fill="both", expand=True)
    root.mainloop()
