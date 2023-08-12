import tkinter as tk
from src._classes import TopLevel, Frame
from tkinter.colorchooser import askcolor

class TableWindow(TopLevel):
    def __init__(self, parent, mode: str, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.mode = mode
        self.title('Periodic Table')
        self.ptb = Table(self, self.mode, bd=1, relief=tk.RAISED)
        self.ptb.loadElements()
        self.ptb.pack(side=tk.TOP)
        if mode=='colour':
            self.eqColour = tk.Button(self, text='Equation Objects', relief=tk.RAISED, bg='light gray', fg =self._PeriodicTable.equationCol, command = lambda: self.equationColourChange())
            self.eqColour.pack(side=tk.LEFT,padx=2, pady=2, fill=tk.X)
            self.saveCol = tk.Button(self, text='Save Colour Confid', relief=tk.RAISED, bg='light gray', fg =self._PeriodicTable.equationCol, command = lambda: self._PeriodicTable.ptb.writeColours())
            self.eqColour.pack(side=tk.LEFT,padx=2, pady=2, fill=tk.X)
            self.close = tk.Button(self, text="Close", relief=tk.RAISED, bg='light gray', command= lambda: self.destroy())
            self.close.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.X)

    def equationColourChange(self) -> None:
        colour = askcolor(title="Tkinter Color Chooser")
        self._PeriodicTable.equationCol = colour[1]
        self.eqColour.configure(fg=colour[1])
        self._parent.sideBar().updateEqButtons()
    
    def saveCol(self) -> None:
        self._PeriodicTable.ptb.writeColours()

class Table(Frame):
    def __init__(self, parent, mode: str, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.mode=mode
        self.elements = []
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
    
    def loadElements(self) -> None:
        for elem in list(self._PeriodicTable):
            elembox = ElementBox(self, self.mode, bd=1, relief=tk.RAISED, width=50, height=50)
            elembox.pack_propagate(False)
            elembox.setElement(elem.num)
            elembox.drawElement()
            self.elements.append(elembox)
        
        for frame in self.elements:
            frame.grid(row=frame.pos[0], column=frame.pos[1], padx=0.5, pady=0.5)
        
        padder = tk.Frame(self, width=50, height=50)
        padder.pack_propagate(False)
        padder.grid(row=7, column=1, padx=0.5, pady=0.5)

class ElementBox(Frame):
    def __init__(self, parent, mode: str, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.mode = mode
        self.vName = tk.StringVar()
        self.vSymbol = tk.StringVar()
        self.vMass = tk.StringVar()
        self.vAnum = tk.StringVar()
        self.bind('<ButtonRelease-1>', self.mouseDown)

    def setElement(self, element: int) -> None:
        self.element = element
        self.vName.set(self._PeriodicTable.atomNo(self.element).name)
        self.vSymbol.set(self._PeriodicTable.atomNo(self.element).symbol)
        self.vAnum.set(self._PeriodicTable.atomNo(self.element).num)
        self.vMass.set(round(self._PeriodicTable.atomNo(self.element).mass,2))
        self.pos = self._PeriodicTable.atomNo(self.element).pos
    
    def drawElement(self) -> None:
        self.topBar = tk.Frame(self, width=50)
        self.topBar.bind("<ButtonRelease-1>", self.mouseDown)
        self.topBar.pack(side=tk.TOP, pady=(2,0))
        
        self.dispAnum = tk.Label(self.topBar, textvariable=self.vAnum, font=('Helvetica','7','bold'))
        self.dispAnum.bind("<ButtonRelease-1>", self.mouseDown)
        self.dispAnum.pack(side=tk.LEFT)
        
        self.dispMass = tk.Label(self.topBar, textvariable=self.vMass, font=('Helvetica','7','bold'))
        self.dispMass.bind("<ButtonRelease-1>", self.mouseDown)
        self.dispMass.pack(side=tk.RIGHT)
        
        self.dispName = tk.Label(self, textvariable=self.vName, font=('Helvetica','6','bold'))
        self.dispName.bind("<ButtonRelease-1>", self.mouseDown)
        self.dispName.pack(side=tk.BOTTOM, pady=(0,2))
        
        self.dispSym = tk.Label(self, textvariable=self.vSymbol, font=('Helvetica','11','bold'), fg=self._PeriodicTable.atomNo(self.element).colour)
        self.dispSym.bind("<ButtonRelease-1>", self.mouseDown)
        self.dispSym.pack(anchor=tk.CENTER)
    
    def mouseDown(self, e: tk.Event) -> None:
        if self.mode == 'colour':
            colour = askcolor(title="Tkinter Color Chooser")
            self._PeriodicTable.atomNo(self.element).setColour(colour[1])
            self.dispSym.configure(fg=colour[1])
            self._parent.parent().parent().sideBar().updateElemButtons(self.element)
        elif self.mode == 'picker':
            self._parent.parent().parent().setAtom(self.element)
            self._parent.parent().destroy()