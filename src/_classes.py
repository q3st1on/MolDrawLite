import tkinter as tk
import platform
from src._atomDicts import PeriodicTableClass, Atom

### THE CLASSES FILE CONTAINS CLASSES FROM WHICH THE WIDGETS DISPLAYED WILL INHERENT. THESE CLASSES ARE NEVER, UNDER ANY CIRCUMSTANCES, TO BE INSTANCED DIRECTLY.
### IF YOU NEED ADDITIONAL FUNCTIONALITY, MAKE ADDITIONAL PARENT CLASSES. DO NOT CREATE DISPLAYED WIDGETS DIRECTLY FROM TKINTER CLASSES.

class TopLevel(tk.Toplevel): # the parent class for all additional toplevel windows spawned such as the periodic table selection windows
    def __init__(self, parent, *args, **kwargs) -> None:
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self): # function to expose parent of instace
        return self._parent

    def periodicTable(self) -> PeriodicTableClass: # references parent's PeriodicTable instace. used to make the MolDrawLite instace accesible globally
        return self._PeriodicTable

class Canvas(tk.Canvas): # Parent of all canvas widgets
    def __init__(self, parent, *args, **kwargs) -> None:
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self): # function to expose parent of instace
        return self._parent
    
    def periodicTable(self) -> PeriodicTableClass: # references parent's PeriodicTable instace. used to make the MolDrawLite instace accesible globally
        return self._PeriodicTable
    
    def drawArc(self, coords: tuple[int, int], r: int, angles: tuple[int, int], width: int, tag: str): # Draws arcs, pretty self explanatory, used for brackets around polymers
        x,y = coords
        t0, t1 = angles
        return self.create_arc(x-(r//2), y-r, x+(r//2), y+r, start=t0, extent=t1, style='arc', width=width, tags=tag)

class ButtonCanvas(Canvas): # used for small canvas buttons such as those on the sidebar menu
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
    
    def findXCenter(self, item: int) -> float: # x offset helper for centering text
        coords = self.bbox(item)
        xOffset = (self.winfo_reqwidth() / 2) - ((coords[2] - coords[0]) / 2)
        return xOffset
    
    def findYCenter(self, item: int) -> float: # y offset helper for centering text
        coords = self.bbox(item)
        yOffset = (self.winfo_reqheight() / 2) - ((coords[3] - coords[1]) / 2)
        return yOffset

    def findCenter(self, item: int) -> tuple[float, float]: # combined offset helper for centering text
        return (self.findXCenter(item), self.findYCenter(item))
    
    def moveItem(self, item: int, coords: list[float]) -> None: # self.move wrapper to parse generated offsets correctly
        self.move(item, coords[0]/2, -coords[1]*2)

class LiveCanvas(Canvas): # class for the main drawing canvas, hass a lot of temporary variables for use when drawing objects
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self._baseCoords: tuple[int | float, int | float]
        self._oldLine: int = 0

        self._arcBaseCoords: tuple[int | float, int | float]
        self._oldArc: int = 0

        self._oldLetterCoords: tuple[int | float, int | float]
        self._oldLetter: int = 0

        self._atomCenters: list[tuple[int | float, int | float], ...] = []
        self._bondEndsOpen: list[tuple[int | float, int | float], ...] = []

        self._oldEqCoords: tuple[int | float, int | float]
        self._oldEqObjs: list[int] 

        self._bondCount: int = 0
        self._atomCount: int = 0
        self._eqObjCount: int = 0
        
    def stateClear(self) -> None: # used when clearing canvas to ensure that relevant state variables are cleared as well. prevents rouge snapping and similar bugs
        self._atomCenters = []
        self._bondEndsOpen = []
        self._bondCount = 0
        self._atomCount = 0
        self._eqObjCount = 0

class Frame(tk.Frame): # parent of every frame used.
    def __init__(self, parent, *args, **kwargs) -> None:
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._PeriodicTable = self._parent.periodicTable()
    
    def parent(self): # function to expose parent of instace
        return self._parent

    def periodicTable(self) -> PeriodicTableClass: # references parent's PeriodicTable instace. used to make the MolDrawLite instace accesible globally
        return self._PeriodicTable


class App(tk.Tk): # parent class of the main MolDrawLite class. Partially sets up state.
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
        self._imageX: int
        self._imageY: int
            
    def periodicTable(self) -> PeriodicTableClass: # references parent's PeriodicTable instace. used to make the MolDrawLite instace accesible globally
        return self._PeriodicTable

    def element(self) -> str: # Exposes the currently selected element
        return int(self._element.get())

    def getElement(self) -> Atom: # exposes the currently selected element's Atom instance
        return self._PeriodicTable.atomNo(self.element())
    
    def bondNo(self) -> int: # exposes currently selected bond count
        return self._bondNo
    
    def eqMode(self) -> str: # exposes currently selected equation mode
        return self._eqMode