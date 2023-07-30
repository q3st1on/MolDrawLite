import tkinter as tk
import platform
from src._atomDicts import PeriodicTableClass

class TopLevel(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self):
        return self._parent

    def periodicTable(self):
        return self._PeriodicTable

class Canvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self):
        return self._parent
    
    def periodicTable(self):
        return self._PeriodicTable

class ButtonCanvas(Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
    
    def findXCenter(self, item):
        coords = self.bbox(item)
        xOffset = (self.winfo_reqwidth() / 2) - ((coords[2] - coords[0]) / 2)
        return xOffset
    
    def findYCenter(self, item):
        coords = self.bbox(item)
        yOffset = (self.winfo_reqheight() / 2) - ((coords[3] - coords[1]) / 2)
        return yOffset

    def findCenter(self, item):
        return (self.findXCenter(item), self.findYCenter(item))
    
    def moveItem(self, item, coords):
        self.move(item, coords[0]/2, -coords[1]*2)

class LiveCanvas(Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._baseCoords = None
        self._oldLine = None

        self._oldLetter = None
        self._oldLetterCoords = None

        self._atomCenters = []
        self._bondEndsOpen = []

        self._oldEqCoords = None
        self._oldEqObjs = []

        self._bondCount = 0
        self._atomCount = 0
        self._eqObjCount = 0
        
    def stateClear(self):
        self._atomCenters = []
        self._bondEndsOpen = []
        self._bondCount = 0
        self._atomCount = 0
        self._eqObjCount = 0

class Frame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self):
        return self._parent

    def periodicTable(self):
        return self._PeriodicTable


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self._PeriodicTable = PeriodicTableClass()

        self._element = tk.DoubleVar(value='6')

        self._stateSymbol = 's'
        self._mode = 'atom'
        self._bondNo = 1
        self._eqMode = '+'
        self._keyBuff = ""    
        self._arch = platform.release()
            
    def periodicTable(self):
        return self._PeriodicTable

    def element(self):
        return int(self._element.get())

    def getElement(self):
        return self._PeriodicTable.atomNo(self.element())
    
    def bondNo(self):
        return self._bondNo
    
    def eqMode(self):
        return self._eqMode