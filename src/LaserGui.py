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

        menu1.add_command(label="Reset", command=self.reset)
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
        self.tab.columnconfigure(1,weight=1)
        self.tab.columnconfigure(2,weight=1)
        self.tab.rowconfigure(0,weight=1)
        self.tab.pack(fill="both")
        self.tabPanel.add(self.tab,text="Tab" + str(self.tabCount))
        self.tabCount = self.tabCount+1
        self.controlPane = tk.Frame(self.tab)
        self.controlPane.grid(column=0,row=0)
        
        self.label1 = tk.Label(self.controlPane, text="Wlax1")
        self.label1.pack()
        self.entry1 = Entry(self.controlPane)
        self.entry1.pack()

        self.label2 = tk.Label(self.controlPane, text="Wlax2")
        self.label2.pack()
        self.entry2 = Entry(self.controlPane)
        self.entry2.pack()

        self.label3 = tk.Label(self.controlPane, text="Taxcp")
        self.label3.pack()
        self.entry3 = Entry(self.controlPane)
        self.entry3.pack()
        
        btn_apply = Button(self.controlPane, text="truncate", command=self.apply_button_action)
        btn_apply.pack()
        
        self.graph1 = tk.Frame(self.tab)
        self.graph2 = tk.Frame(self.tab)
        self.graph1.grid(column=1,row=0,sticky="nsew")
        self.graph2.grid(column=2,row=0,sticky="nsew")
    
    def apply_button_action(self):
        controlThread = Thread(target=self.truncate_graph_thread_exec, daemon = True)
        controlThread.start()
    
    def truncate_graph_thread_exec(self):
        self.fig3 = rawTAspectrum.load_truncated_chart(int(self.entry1.get()), int(self.entry2.get()), int(self.entry3.get()))
        self.after(0,self.create_truncation_tab)
    
    def create_truncation_tab(self):
        self.update()
        self.truncTab = tk.Frame(self.tabPanel)
        self.truncTab.pack(fill="both")
        self.tabPanel.add(self.truncTab,text="Tab" + str(self.tabCount))
        self.tabCount = self.tabCount+1
        self.graph3 = tk.Frame(self.truncTab)
        self.graph3.pack()
        canvas = FigureCanvasTkAgg(self.fig3, master=self.graph3)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas.draw()
        self.update()

    #opens data file and funs analysis
    def open_file(self):
        self.fileName = filedialog.askopenfilename(initialdir="/C:", title="Select a File", filetypes=(("DAT files", "*.dat"),("All files", "*.*")))
        #rawTAspectrum.load_chart(self.fileName)
        controlThread = Thread(target=self.dat_file_thread_exec, daemon=True)
        self.progressBar = ttk.Progressbar(root,orient=tk.HORIZONTAL,length=200,mode="indeterminate",takefocus=True,maximum=100)
        controlThread.start()
        self.progressBar.start()
        self.progressBar.pack()

    
    def get_tab_count(self):
        return self.tabCount
    
    def dat_file_thread_exec(self):
        #variable for progress bar on GUI
        self.update() 
        rawTAspectrum.load_data_file(self.fileName)
        self.fig1 = rawTAspectrum.load_raw_data()
        self.fig2 = rawTAspectrum.load_data_without_axes()
        self.after(0,self.draw_plot)
    
    def draw_plot(self):
        self.progressBar.stop()
        self.progressBar.destroy()
        self.create_graph1()
        canvas = FigureCanvasTkAgg(self.fig1, master=self.graph1)
        canvas2 = FigureCanvasTkAgg(self.fig2,master=self.graph2)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.graph1)
        toolbar2 = NavigationToolbar2Tk(canvas2, self.graph2)
        toolbar.update()
        toolbar2.update()
        canvas.draw()
        canvas2.draw()
        self.update()

    def reset(self):
        self.tabPanel.destroy()                             # clears out the tab panel
        self.tabPanel = ttk.Notebook(self)                  # resetting the tab panel
        self.tabPanel.pack(fill="both", expand=True)        


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
