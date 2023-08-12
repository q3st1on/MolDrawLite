import tkinter as tk
import platform
from src._atomDicts import PeriodicTableClass, Atom

class TopLevel(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs) -> None:
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self):
        return self._parent

    def periodicTable(self) -> PeriodicTableClass:
        return self._PeriodicTable

class Canvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs) -> None:
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self):
        return self._parent
    
    def periodicTable(self) -> PeriodicTableClass:
        return self._PeriodicTable
    
    def drawArc(self, coords: tuple[int, int], r: int, angles: tuple[int, int], width: int):
        x,y = coords
        t0, t1 = angles
        return self.create_arc(x-(r//2), y-r, x+(r//2), y+r, start=t0, extent=t1, style='arc', width=width)

class ButtonCanvas(Canvas):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
    
    def findXCenter(self, item: int) -> float:
        coords = self.bbox(item)
        xOffset = (self.winfo_reqwidth() / 2) - ((coords[2] - coords[0]) / 2)
        return xOffset
    
    def findYCenter(self, item: int) -> float:
        coords = self.bbox(item)
        yOffset = (self.winfo_reqheight() / 2) - ((coords[3] - coords[1]) / 2)
        return yOffset

    def findCenter(self, item: int) -> tuple[float, float]:
        return (self.findXCenter(item), self.findYCenter(item))
    
    def moveItem(self, item: int, coords: list[float]) -> None:
        self.move(item, coords[0]/2, -coords[1]*2)

class LiveCanvas(Canvas):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self._baseCoords: tuple[int | float, int | float]
        self._oldLine: int

        self._arcBaseCoords: tuple[int | float, int | float]
        self._oldArc: int

        self._oldLetterCoords: tuple[int | float, int | float]
        self._oldLetter: int

        self._atomCenters: list[tuple[int | float, int | float], ...] = []
        self._bondEndsOpen: list[tuple[int | float, int | float], ...] = []

        self._oldEqCoords: tuple[int | float, int | float]
        self._oldEqObjs: list[int]

        self._bondCount: int = 0
        self._atomCount: int = 0
        self._eqObjCount: int = 0
        
    def stateClear(self) -> None:
        self._atomCenters = []
        self._bondEndsOpen = []
        self._bondCount = 0
        self._atomCount = 0
        self._eqObjCount = 0

class Frame(tk.Frame):
    def __init__(self, parent, *args, **kwargs) -> None:
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self):
        return self._parent

    def periodicTable(self) -> PeriodicTableClass:
        return self._PeriodicTable


class App(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)
        self._PeriodicTable = PeriodicTableClass()

        self._element = tk.DoubleVar(value='6')

        self._stateSymbol = 's'
        self._mode = 'atom'
        self._bondNo = 1
        self._arcSide = 'left'
        self._eqMode = '+'
        self._keyBuff = ""    
        self._arch = platform.system()
            
    def periodicTable(self) -> PeriodicTableClass:
        return self._PeriodicTable

    def element(self) -> str:
        return int(self._element.get())

    def getElement(self) -> Atom:
        return self._PeriodicTable.atomNo(self.element())
    
    def bondNo(self) -> int:
        return self._bondNo
    
    def eqMode(self) -> str:
        return self._eqMode