import tkinter as tk
import tkinter.messagebox
from src.atomDicts import periodic_table
from src.canvas import genCanvas
from src.sidemenu import sideMenu
from src.topmenu import topMenu
from src.imageConstruct import imageWindow
from src.ptable import tableWindow
import time

class MolDrawLite(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("MolDrawLite")
        self.resizable(height = None, width = None)
        self.minsize(1280, 720)

        self.element = tk.DoubleVar(value='6')

        self.base_coords = None
        self.old_line = None

        self.old_letter = None
        self.old_letter_coords = None

        self.atomcenters = []
        self.bondendsopen = []

        self.old_eq_coords = None
        self.old_eq_objs = []

        self.bondcount = 0
        self.atomcount = 0
        self.eqobcount = 0

        self.statesymbol = 's'
        self.mode = 'atom'
        self.bondno = 1
        self.eqmode = '+'
        self.keybuff = ""
        
        self.sidebar = sideMenu(self, bd=1, relief=tk.RAISED, width=20)
        self.sidebar.pack(side=tk.LEFT, padx = (4, 8), pady = (8, 8), fill=tk.Y, ipadx=5, ipady=5)

        self.topbar = topMenu(self, bd=1, relief=tk.RAISED, height = 20)
        self.topbar.pack(side=tk.TOP, fill=tk.X, padx=(4, 8), pady=(8, 4), ipadx=5, ipady=5)

        self.canvas = genCanvas(self, bd=1, relief=tk.RAISED, closeenough=2)
        self.canvas.pack(side = tk.BOTTOM, anchor=tk.SE, fill=tk.BOTH, padx = (4, 8), pady = (4, 8), expand=True)

        self.tablewin = tableWindow(self)
        self.tablewin.mainloop()

        self.bind("<KeyPress>", lambda x: self.keydown(x))


    def setBond(self, num):
        self.bondno = num
        self.setMode('bond')
        self.sidebar.updateBond(num)
    
    def setSymbol(self, sym):
        self.eqmode = sym
        self.setMode('equation')
        self.sidebar.updateSymbol(sym)
    
    def setAtom(self, atom):
        self.element.set(atom)
        self.setMode('atom')
        self.sidebar.updateElemHighlight(atom)
    
    def setMode(self, mode):
        self.mode = mode
        match mode:
            case 'ss':
                self.sidebar.deacBond()
                self.sidebar.deacElem()
                self.sidebar.deacSymbol()
            case 'bond':
                self.sidebar.updateBond(self.bondno)
                self.sidebar.deacElem()
                self.sidebar.deacSymbol()
            case 'atom':
                self.sidebar.deacBond()
                self.sidebar.updateElemHighlight(self.element.get())
                self.sidebar.deacSymbol()
            case 'equation':
                self.sidebar.deacBond()
                self.sidebar.deacElem()
                self.sidebar.updateSymbol(self.eqmode)
            case _:
                self.sidebar.deacBond()
                self.sidebar.deacElem()
                self.sidebar.deacSymbol()

        self.topbar.updateMode(mode)
    
    def clear(self):
        self.atomcenters = []
        self.bondendsopen = []
        self.bondcount = 0
        self.atomcount = 0
        self.eqobcount = 0
        self.canvas.delete('all')

    def mousedown(self, e):
        if self.mode == 'bond':
            self.canvas.make_line(e)
        elif self.mode == 'atom':
            self.canvas.make_letter(e)
        elif self.mode == 'equation':
            self.canvas.makeeq(e)
        elif self.mode == 'delete':
            self.canvas.delete("current")

    def mousemove(self, e):
        if self.mode == 'bond':
            self.canvas.draw_line(e)
        elif self.mode == 'atom':
            self.canvas.move_letter(e)
        elif self.mode == 'equation':
            self.canvas.moveeq(e)
        elif self.mode == 'delete':
            self.canvas.delete("current")

    def mouseup(self, e):
        if self.mode == 'bond':
            self.canvas.fix_line(e)
        elif self.mode == 'atom':
            self.canvas.fix_letter(e)
        elif self.mode == 'equation':
            self.canvas.fix_eq(e)

    def keydown(self, e):
        if e.keysym_num == 66: # Shift + b
            self.setMode('bond')
        elif e.keysym_num == 65: # Shift + a
            self.setMode('atom')
        elif e.keysym_num == 69: # Shift + e
            self.setMode('equation')
        elif e.keycode == 22: # backspace
            self.setMode('delete')
        elif e.keycode == 119: # del
            self.canvas.delete('all')
        elif self.mode=='delete':
            if e.keysym_num == 98: # b
                self.setMode('bond')
            elif e.keysym_num == 97: # a
                self.setMode('atom')
            elif e.keysym_num == 101: # e
                self.setMode('equation')
        elif self.mode=='bond':
            match e.keycode:
                case 10: # 1
                    self.setBond(1)
                case 11: # 2
                    self.setBond(2)
                case 12: # 3
                    self.setBond(3)
                case 13: # 4
                    self.setBond(4)
                case 14: # 5
                    self.setBond(5)
                case _:
                    pass
        elif self.mode=='atom':
            if e.keysym.isdigit():
                self.keybuff += e.keysym
            elif e.keysym_num == 65293:
                self.atomInput()
            else:
                match e.keycode:
                    case 54: # c
                        self.setAtom(6)
                    case 43: #h
                        self.setAtom(1)
                    case 57: #n
                        self.setAtom(7)
                    case 32: #o
                        self.setAtom(8)
                    case _:
                        pass
        elif self.mode=='equation':
            match e.keysym_num:
                case 43: # +
                    self.setSymbol('+')
                case 61: # =
                    self.setSymbol('equilibrium')
                case 46: # >
                    self.setSymbol('forward')
                case _:
                    pass

    def selectedelem(self):
        if self.element.get() != '':
            elem = int(self.element.get())
            if (elem <= 118) & (elem >=1):
                return periodic_table[elem-1]['symbol']
        return 'C'

    def elemcolour(self):
        if self.element.get() != '':
            elem = int(self.element.get())
            if (elem <= 118) & (elem >=1):
                try:
                    return periodic_table[elem-1]['colour']
                except:
                    return 'black'
        return 'gray11'

    def atomInput(self):
        anum = int(self.keybuff)
        if anum in range(1, 119):
            self.element.set(anum)
        else:
            tkinter.messagebox.showwarning('Select Element Error', f"{anum} is not a valid atomic number")
        self.keybuff = ""
        self.sidebar.updateElemHighlight(self.element.get())
    
    def genImage(self):
        info = [self.canvas.gettags(i) for i in self.canvas.find_all()]
        if len(info) == 0:
            tkinter.messagebox.showwarning("Empty Canvas!", "Empty Canvas!")
        else:
            self.imagePopUp = imageWindow(self, info)
            self.imagePopUp.mainloop()

    def getElement(self):
        return self.element