import rawTAspectrum
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from threading import Thread
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter.filedialog import asksaveasfile

import os

class Project(tk.Frame):
    def __init__(self,parent):
        #initialize GUI variables
        tk.Frame.__init__(self,parent)

        #class variables
        self.tabCount =1
        self.tabPanel = ttk.Notebook(self)
        self.tabPanel.pack(pady=15)

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
        self.tab = tk.Frame(self.tabPanel, width=970, height=680)
        self.tab.pack(fill="both",expand=1)
        self.tabPanel.add(self.tab,text="Tab" + str(self.tabCount))
        self.tabCount = self.tabCount+1

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
        fig = rawTAspectrum.load_chart()
        progressBar.stop()
        progressBar.destroy()
        self.after(0,self.draw_plot)
    
    def draw_plot(self):
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.draw()
        self.update()


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
