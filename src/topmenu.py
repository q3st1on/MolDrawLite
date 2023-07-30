import tkinter as tk
from src.classes import Frame

class TopMenu(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.bond = tk.Button(self, text="Bond", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('bond'))
        self.bond.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self.atom = tk.Button(self, text="Atom", relief=tk.RAISED, bg='gray', command= lambda: self._parent.setMode('atom'))
        self.atom.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self.equation = tk.Button(self, text="Equation", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('equation'))
        self.equation.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self.subscript = tk.Button(self, text="Subscript", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('ss'))
        self.subscript.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self.image = tk.Button(self, text="Save As Image", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.genImage())
        self.image.pack(side = tk.LEFT, padx=2, pady=2, fill=tk.X)

        self.colour = tk.Button(self, text="Change Colours", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.createTable('colour'))
        self.colour.pack(side = tk.LEFT, padx=2, pady=2, fill=tk.X)

        self.clear = tk.Button(self, text="Clear", relief=tk.RAISED, command= lambda: self._parent.canvas.clearAll())
        self.clear.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.X)

        self.delete = tk.Button(self, text="Delete", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('delete'))
        self.delete.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.X)

    def updateMode(self, mode):
        match mode:
            case 'atom':
                self.atom.config(bg='gray')
                self.bond.config(bg='light gray')
                self.equation.config(bg='light gray')
                self.delete.config(bg='light gray') 
                self.subscript.config(bg='light gray')
            case 'bond':
                self.atom.config(bg='light gray')
                self.bond.config(bg='gray')
                self.equation.config(bg='light gray')
                self.delete.config(bg='light gray') 
                self.subscript.config(bg='light gray')
            case 'equation':
                self.atom.config(bg='light gray')
                self.bond.config(bg='light gray')
                self.equation.config(bg='gray') 
                self.delete.config(bg='light gray') 
                self.subscript.config(bg='light gray')
            case 'delete':
                self.atom.config(bg='light gray')
                self.bond.config(bg='light gray')
                self.equation.config(bg='light gray') 
                self.delete.config(bg='gray')
                self.subscript.config(bg='light gray')
            case 'ss':
                self.atom.config(bg='light gray')
                self.bond.config(bg='light gray')
                self.equation.config(bg='light gray') 
                self.delete.config(bg='light gray')
                self.subscript.config(bg='gray')
            case _:
                self.atom.config(bg='light gray')
                self.bond.config(bg='light gray')
                self.equation.config(bg='light gray') 
                self.delete.config(bg='light gray')
                self.subscript.config(bg='light gray')
