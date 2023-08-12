import tkinter as tk
from src._classes import Frame

class TopMenu(Frame):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        self._bond = tk.Button(self, text="Bond", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('bond'))
        self._bond.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self._atom = tk.Button(self, text="Atom", relief=tk.RAISED, bg='gray', command= lambda: self._parent.setMode('atom'))
        self._atom.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self._equation = tk.Button(self, text="Equation", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('equation'))
        self._equation.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self._polymer = tk.Button(self, text="Polymer", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('polymer'))
        self._polymer.pack(side=tk.LEFT, padx=2, pady=2, fill=tk.X)

        self._image = tk.Button(self, text="Save As Image", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.genImage())
        self._image.pack(side = tk.LEFT, padx=2, pady=2, fill=tk.X)

        self._colour = tk.Button(self, text="Change Colours", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.createTable('colour'))
        self._colour.pack(side = tk.LEFT, padx=2, pady=2, fill=tk.X)

        self._clear = tk.Button(self, text="Clear", relief=tk.RAISED, command= lambda: self._parent.canvas().clearAll())
        self._clear.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.X)

        self._delete = tk.Button(self, text="Delete", relief=tk.RAISED, bg='light gray', command= lambda: self._parent.setMode('delete'))
        self._delete.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.X)

    def updateMode(self, mode: str) -> None:
        match mode:
            case 'atom':
                self._atom.config(bg='gray')
                self._bond.config(bg='light gray')
                self._equation.config(bg='light gray')
                self._delete.config(bg='light gray') 
                self._polymer.config(bg='light gray')
            case 'bond':
                self._atom.config(bg='light gray')
                self._bond.config(bg='gray')
                self._equation.config(bg='light gray')
                self._delete.config(bg='light gray') 
                self._polymer.config(bg='light gray')
            case 'equation':
                self._atom.config(bg='light gray')
                self._bond.config(bg='light gray')
                self._equation.config(bg='gray') 
                self._delete.config(bg='light gray') 
                self._polymer.config(bg='light gray')
            case 'delete':
                self._atom.config(bg='light gray')
                self._bond.config(bg='light gray')
                self._equation.config(bg='light gray') 
                self._delete.config(bg='gray')
                self._polymer.config(bg='light gray')
            case 'polymer':
                self._atom.config(bg='light gray')
                self._bond.config(bg='light gray')
                self._equation.config(bg='light gray') 
                self._delete.config(bg='light gray')
                self._polymer.config(bg='gray')
            case _:
                self._atom.config(bg='light gray')
                self._bond.config(bg='light gray')
                self._equation.config(bg='light gray') 
                self._delete.config(bg='light gray')
                self._polymer.config(bg='light gray')
