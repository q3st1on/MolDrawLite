
from src.imageConstruct import imageWindow
from src.atomDicts import PeriodicTable
from src.ptable import tableWindow
from src.settings import createCFG
from src.sidemenu import sideMenu
from src.canvas import genCanvas
from src.topmenu import topMenu
import tkinter.messagebox
import tkinter as tk
import time
import json
import os

class MolDrawLite(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("MolDrawLite")
        self.resizable(height = None, width = None)
        self.minsize(1280, 720)

        self.element = tk.DoubleVar(value='6')
        self._element = 6

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
        
        self.loadCFG()
        self.bind("<KeyPress>", lambda x: self.keydown(x))

    def loadCFG(self):
        path = os.path.realpath(__file__)+'/config.json'
        if os.path.isfile(path):
            with open(os.path.dirname(path, 'r')) as f:
                self.config = json.loads(f.read())
        else:
            cfg = createCFG(self)
            cfg.attributes('-type', 'dialog')
            cfg.mainloop()
            with open(os.path.dirname(path, 'r')) as f:
                f.write(json.dumps(self.config))
    


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
        self._element = atom
        self.setMode('atom')
        self.sidebar.updateElemHighlight(self._element)
    
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
                self.sidebar.updateElemHighlight(self._element)
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
        if e.keysym_num == self.config['shift+b']: # Shift + b
            self.setMode('bond')
        elif e.keysym_num == self.config['shift+a']: # Shift + a
            self.setMode('atom')
        elif e.keysym_num == self.config['shift+e']: # Shift + e
            self.setMode('equation')
        elif e.keycode == self.config['backspace']: # backspace
            self.setMode('delete')
        elif e.keycode == self.config['delete']: # del
            self.canvas.clearAll()
        elif self.mode=='delete':
            if e.keysym_num == self.config['b']: # b
                self.setMode('bond')
            elif e.keysym_num == self.config['a']: # a
                self.setMode('atom')
            elif e.keysym_num == self.config['e']: # e
                self.setMode('equation')

        elif self.mode=='bond':
            if e.keycode== self.config['1']: # 1
                self.setBond(1)
            elif e.keycode== self.config['2']: # 2
                self.setBond(2)
            elif e.keycode== self.config['3']: # 3
                self.setBond(3)
            elif e.keycode== self.config['4']: # 4
                self.setBond(4)
            elif e.keycode== self.config['5']: # 5
                self.setBond(5)

        elif self.mode=='atom':
            if e.keysym.isdigit():
                self.keybuff += e.keysym
            elif e.keysym_num == self.config['enter']:
                self.atomInput()
            else:
                if e.keycode== self.config['c']: # c
                    self.setAtom(6)
                elif e.keycode== self.config['h']: #h
                    self.setAtom(1)
                elif e.keycode== self.config['n']: #n
                    self.setAtom(7)
                elif e.keycode== self.config['o']: #o
                    self.setAtom(8)
                elif e.keycode== self.config['r']: #r
                    self.setAtom(0)
                elif e.keysym_num== self.config['a']: #a
                    self.createTable('picker')

        elif self.mode=='equation':
            if e.keysym_num== self.config['+']: # +
                self.setSymbol('+')
            elif e.keysym_num== self.config['=']: # =
                self.setSymbol('equilibrium')
            elif e.keysym_num== self.config['>']: # >
                self.setSymbol('forward')

    
    def atomInput(self):
        anum = int(self.keybuff)
        if anum in range(1, 119):
            self.element.set(anum)
            self._element = anum
        else:
            tkinter.messagebox.showwarning('Select Element Error', f"{anum} is not a valid atomic number")
        self.keybuff = ""
        self.sidebar.updateElemHighlight(self._element)
    
    def genImage(self):
        info = [self.canvas.gettags(i) for i in self.canvas.find_all()]
        if len(info) == 0:
            tkinter.messagebox.showwarning("Empty Canvas!", "Empty Canvas!")
        else:
            self.imagePopUp = imageWindow(self, info)
            self.imagePopUp.mainloop()

    def getElement(self):
        return PeriodicTable.atomNo(self._element)
    
    def createTable(self, mode):
        self.tablewin = tableWindow(self, mode)
        self.tablewin.attributes('-type', 'dialog')
        self.tablewin.mainloop()
