
from src._imageConstruct import ImageWindow
from src._atomDicts import PeriodicTableClass
from src._ptable import TableWindow
from src._sidemenu import SideMenu
from src._canvas import GenCanvas
from src._classes import App
from src._topmenu import TopMenu
import tkinter.messagebox
import tkinter as tk
import time
import json
import os

class MolDrawLite(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("MolDrawLite")
        self.resizable(height = None, width = None)
        self.minsize(1280, 720)
        
        self._sideBar = SideMenu(self, bd=1, relief=tk.RAISED, width=20)
        self._sideBar.pack(side=tk.LEFT, padx = (4, 8), pady = (8, 8), fill=tk.Y, ipadx=5, ipady=5)

        self._topBar = TopMenu(self, bd=1, relief=tk.RAISED, height = 20)
        self._topBar.pack(side=tk.TOP, fill=tk.X, padx=(4, 8), pady=(8, 4), ipadx=5, ipady=5)

        self._canvas = GenCanvas(self, bd=1, relief=tk.RAISED, closeenough=2)
        self._canvas.pack(side = tk.BOTTOM, anchor=tk.SE, fill=tk.BOTH, padx = (4, 8), pady = (4, 8), expand=True)
        
        self.bind("<KeyPress>", lambda x: self.keyDown(x))

    def setBond(self, num):
        self._bondNo = num
        self.setMode('bond')
        self._sideBar.updateBond(num)
    
    def setSymbol(self, sym):
        self._eqMode = sym
        self.setMode('equation')
        self._sideBar.updateSymbol(sym)
    
    def setAtom(self, atom):
        self._element.set(atom)
        self.setMode('atom')
        self._sideBar.updateElemHighlight(self.element())
    
    def setMode(self, mode):
        self._mode = mode
        match mode:
            case 'ss':
                self._sideBar.deacBond()
                self._sideBar.deacElem()
                self._sideBar.deacSymbol()
            case 'bond':
                self._sideBar.updateBond(self._bondNo)
                self._sideBar.deacElem()
                self._sideBar.deacSymbol()
            case 'atom':
                self._sideBar.deacBond()
                self._sideBar.updateElemHighlight(self.element())
                self._sideBar.deacSymbol()
            case 'equation':
                self._sideBar.deacBond()
                self._sideBar.deacElem()
                self._sideBar.updateSymbol(self._eqMode)
            case _:
                self._sideBar.deacBond()
                self._sideBar.deacElem()
                self._sideBar.deacSymbol()

        self._topBar.updateMode(mode)

    def mouseDown(self, e):
        match self._mode:
            case 'bond':
                self._canvas.makeLine(e)
            case 'atom':
                self._canvas.makeLetter(e)
            case 'equation':
                self._canvas.makeEq(e)
            case 'delete':
                self._canvas.delete("current")

    def mouseMove(self, e):
        match self._mode:
            case 'bond':
                self._canvas.drawLine(e)
            case 'atom':
                self._canvas.moveLetter(e)
            case 'equation':
                self._canvas.moveEq(e)
            case 'delete':
                self._canvas.delete("current")

    def mouseUp(self, e):
        match self._mode:
            case 'bond':
                self._canvas.fixLine(e)
            case 'atom':
                self._canvas.fixLetter(e)
            case 'equation':
                self._canvas.fixEq(e)

    def keyDown(self, e):
        print(e.keysym)
        match e.keysym:
            case "B":
                self.setMode('bond')
                
            case "A":
                self.setMode('atom')
                
            case "E":
                self.setMode('equation')
                
            case "BackSpace":
                self.setMode('delete')
                
            case "Delete":
                self._canvas.clearAll()
                
            case _:
                match self._mode:
                    case 'delete':
                        match e.keysym:
                            case 'b':
                                self.setMode('bond')
                            case 'a':
                                self.setMode('atom')
                            case 'e':
                                self.setMode('equation')
                            case _:
                                pass
                            
                    case 'bond':
                        if e.keysym in [str(i) for i in range(1,6)]:
                            self.setBond(int(e.keysym))
                        else:
                            pass
                        
                    case 'atom':
                        if e.keysym.isdigit():
                            self._keyBuff += e.keysym
                        else:
                            match e.keysym:
                                case "Enter":
                                    self.atomInput()
                                case 'c': # c
                                    self.setAtom(6)
                                case 'h': #h
                                    self.setAtom(1)
                                case 'n': #n
                                    self.setAtom(7)
                                case 'o': #o
                                    self.setAtom(8)
                                case 'r': #r
                                    self.setAtom(0)
                                case 'a': #a
                                    self.createTable('picker')
                                case _:
                                    pass
                                
                    case 'equation':
                        match e.keysym:
                            case 'plus':
                                self.setSymbol('+')
                            case 'equal':
                                self.setSymbol('equilibrium')
                            case 'greater':
                                self.setSymbol('forward')
                            case _:
                                pass

                    case _:
                        pass
    
    def atomInput(self):
        anum = int(self._keyBuff)
        if anum in range(1, 119):
            self._element.set(anum)
        else:
            tkinter.messagebox.showwarning('Select Element Error', f"{anum} is not a valid atomic number")
        self._keyBuff = ""
        self._sideBar.updateElemHighlight(self.element())
    
    def genImage(self):
        info = [self._canvas.gettags(i) for i in self._canvas.find_all()]
        if len(info) == 0:
            tkinter.messagebox.showwarning("Empty Canvas!", "Empty Canvas!")
        else:
            self.imagePopUp = ImageWindow(self, info)
            self.imagePopUp.mainloop()
    
    def createTable(self, mode):
        self.tablewin = TableWindow(self, mode)
        print(self._arch)
        if self._arch == 'Linux':
            self.tablewin.attributes('-type', 'dialog')
        self.tablewin.attributes('-topmost', True)
        self.tablewin.mainloop()

    def canvas(self):
        return self._canvas
    
    def sideBar(self):
        return self._sideBar
    
    def topBar(self):
        return self._topBar