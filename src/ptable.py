import tkinter as tk
from tkinter.colorchooser import askcolor
from src.atomDicts import PeriodicTable

class tableWindow(tk.Toplevel):
    def __init__(self, parent, mode, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mode = mode
        self.title('Periodic Table')
        self.ptb = table(self, self.mode, bd=1, relief=tk.RAISED)
        self.ptb.loadElements()
        self.ptb.pack(side=tk.TOP)
        if mode=='colour':
            self.eqColour = tk.Button(self, text='Equation Objects', relief=tk.RAISED, bg='light gray', fg =PeriodicTable.equationCol, command = lambda: self.equationColourChange())
            self.eqColour.pack(side=tk.LEFT,padx=2, pady=2, fill=tk.X)
            self.saveCol = tk.Button(self, text='Save Colour Confid', relief=tk.RAISED, bg='light gray', fg =PeriodicTable.equationCol, command = lambda: PeriodicTable.ptb.writeColours())
            self.eqColour.pack(side=tk.LEFT,padx=2, pady=2, fill=tk.X)
            self.close = tk.Button(self, text="Close", relief=tk.RAISED, bg='light gray', command= lambda: self.destroy())
            self.close.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.X)

    def equationColourChange(self):
        colour = askcolor(title="Tkinter Color Chooser")
        PeriodicTable.equationCol = colour[1]
        self.eqColour.configure(fg=colour[1])
        self.parent.sidebar.updateEqButtons()
    
    def saveCol(self):
        PeriodicTable.ptb.writeColours()

class table(tk.Frame):
    def __init__(self, parent, mode, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mode=mode
        self.elements = []
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
    
    def loadElements(self):
        for elem in list(PeriodicTable):
            elembox = elementBox(self, self.mode, bd=1, relief=tk.RAISED, width=50, height=50)
            elembox.pack_propagate(False)
            elembox.setElement(elem.num)
            elembox.drawElement()
            self.elements.append(elembox)
        
        for frame in self.elements:
            frame.grid(row=frame.pos[0], column=frame.pos[1], padx=0.5, pady=0.5)
        
        padder = tk.Frame(self, width=50, height=50)
        padder.pack_propagate(False)
        padder.grid(row=7, column=1, padx=0.5, pady=0.5)

class elementBox(tk.Frame):
    def __init__(self, parent, mode, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mode = mode
        self.vName = tk.StringVar()
        self.vSymbol = tk.StringVar()
        self.vMass = tk.StringVar()
        self.vAnum = tk.StringVar()
        self.bind('<ButtonRelease-1>', self.mouseDown)

    def setElement(self, element):
        self.element = element
        self.vName.set(PeriodicTable.atomNo(self.element).name)
        self.vSymbol.set(PeriodicTable.atomNo(self.element).symbol)
        self.vAnum.set(PeriodicTable.atomNo(self.element).num)
        self.vMass.set(round(PeriodicTable.atomNo(self.element).mass,2))
        self.pos = PeriodicTable.atomNo(self.element).pos
    
    def drawElement(self):
        self.topBar = tk.Frame(self, width=50)
        self.topBar.pack(side=tk.TOP, pady=(2,0))
        self.dispAnum = tk.Label(self.topBar, textvariable=self.vAnum, font=('Helvetica','7','bold'))
        self.dispAnum.pack(side=tk.LEFT)
        self.dispMass = tk.Label(self.topBar, textvariable=self.vMass, font=('Helvetica','7','bold'))
        self.dispMass.pack(side=tk.RIGHT)
        self.dispName = tk.Label(self, textvariable=self.vName, font=('Helvetica','6','normal'))
        self.dispName.pack(side=tk.BOTTOM, pady=(0,2))
        self.dispSym = tk.Label(self, textvariable=self.vSymbol, font=('Helvetica','16','bold'), fg=PeriodicTable.atomNo(self.element).colour)
        self.dispSym.pack(anchor=tk.CENTER)
    
    def mouseDown(self, e):
        if self.mode == 'colour':
            colour = askcolor(title="Tkinter Color Chooser")
            PeriodicTable.atomNo(self.element).setColour(colour[1])
            self.dispSym.configure(fg=colour[1])
            self.parent.parent.parent.sidebar.updateElemButtons(self.element)
        elif self.mode == 'picker':
            self.parent.parent.parent.setAtom(self.element)
            self.parent.parent.destroy()