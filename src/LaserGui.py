import rawTAspectrum
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class Project(tk.Frame):
    def __init__(self,parent):
        #initialize GUI variables
        tk.Frame.__init__(self,parent)

        self.tabCount =1
        self.tabPanel = ttk.Notebook(self)
        self.tabPanel.pack(pady=15)

        myMenu = tk.Menu(self)
        parent.config(menu=myMenu)

        #add menu Items
        menu1 = tk.Menu(myMenu)
        myMenu.add_cascade(label="Menu 1", menu=menu1)
        menu1.add_command(label="Select a file", command=self.OpenFile)

        menu2 = tk.Menu(myMenu)
        myMenu.add_cascade(label="Menu 2", menu=menu2)
        menu2.add_command(label="Menu Item 3", command=emptyCommand)
        menu2.add_command(label="Menu Item 4", command=emptyCommand)


    def createTab(self):
        # created new tabs
        self.tab = tk.Frame(self.tabPanel, width=970, height=680)
        self.tab.pack(fill="both",expand=1)
        self.tabPanel.add(tab,text="Tab" + str(tabCount))

    def OpenFile(self):
        self.fileName = filedialog.askopenfilename(initialdir="/C:", title="Select a File", filetypes=(("DAT files", "*.dat"),("All files", "*.*")))
        rawTAspectrum.plot(self.fileName)
    def emptyCommand():
        pass
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Laser Noise Analysis App')
    root.geometry("1000x700")
    Project(root).pack(fill="both", expand=True)
    root.mainloop()