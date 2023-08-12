from src._util import nearRound, closestNode
from src._classes import LiveCanvas
import tkinter as tk
import math

class GenCanvas(LiveCanvas):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.bind('<Button-1>', self._parent.mouseDown)
        self.bind('<B1-Motion>', self._parent.mouseMove)
        self.bind('<ButtonRelease-1>', self._parent.mouseUp)

    def makeLetter(self, e: tk.Event) -> None:
        x, y = e.x, e.y
        rx, ry = nearRound(e.x, 60), nearRound(e.y, 60)
        if len(self._bondEndsOpen) != 0:
            self._oldLetterCoords = closestNode((x,y), self._bondEndsOpen+[(rx, ry)])
        else:
            self._oldLetterCoords = rx,ry
        x,y = self._oldLetterCoords
        self._oldLetter = self.create_text(x, y, text=self._parent.getElement().symbol, font=('Helvetica','28','bold'), fill=self._parent.getElement().colour, justify=tk.CENTER)

    def moveLetter(self, e: tk.Event) -> None:
        x, y = e.x, e.y
        rx, ry = nearRound(e.x, 60), nearRound(e.y, 60)
        x1, y1 = self._oldLetterCoords
        if (x,y) != (x1, y1):
            if len(self._bondEndsOpen) != 0:
                self._oldLetterCoords = closestNode((x,y), self._bondEndsOpen+[(rx, ry)])
            else:
                self._oldLetterCoords = rx,ry
            self.delete(self._oldLetter)
        x,y = self._oldLetterCoords
        self._oldLetter = self.create_text(x, y, text=self._parent.getElement().symbol, font=('Helvetica','18','bold'), fill=self._parent.getElement().colour, justify=tk.CENTER)

    def fixLetter(self, e: tk.Event) -> None:
        x, y = self._oldLetterCoords
        self.delete(self._oldLetter)
        self.create_text(x, y, text=self._parent.getElement().symbol, font=('Helvetica','18','bold'), fill=self._parent.getElement().colour, justify=tk.CENTER, tags=f"1 {self._parent.getElement().colour.replace(' ', '_')} {self._parent.getElement().symbol} {x} {y}")
        self._atomCenters.append((x,y))
        if self._oldLetterCoords in self._bondEndsOpen:
            self._bondEndsOpen.remove(self._oldLetterCoords)
        self._atomCount += 1

    def makeEq(self, e: tk.Event) -> None:
        x, y = nearRound(e.x, 30), nearRound(e.y, 30)
        self._oldEqCoords = x, y
        if self._parent.eqMode() == '+':
            self._oldEqObjs = [self.create_text(x, y, text='+', font=('Helvetica','20','bold'), fill=self._PeriodicTable.equationCol, justify=tk.CENTER)]
        elif self._parent.eqMode() == 'forward':
            self._oldEqObjs = [self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = self._PeriodicTable.equationCol, width = 3)]
        elif self._parent.eqMode() == 'equilibrium':
            self._oldEqObjs = [self.create_line(x-30, y-4, x+30, y-4, x+24, y-8, x+24, y-4, fill = self._PeriodicTable.equationCol, width = 3, joinstyle=tk.MITER), self.create_line(x-24, y+4, x-24, y+8, x-30, y+4, x+30,y+4, fill = self._PeriodicTable.equationCol, width = 3, joinstyle=tk.MITER)]

    def moveEq(self, e: tk.Event) -> None:
        x, y = nearRound(e.x, 30), nearRound(e.y, 30)
        if self._oldEqCoords != (x, y):
            self._oldEqCoords = (x, y)
            for i in self._oldEqObjs:
                self.delete(i)
            if self._parent.eqMode() == '+':
                self._oldEqObjs = [self.create_text(x, y, text='+', font=('Helvetica','20','bold'), fill=self._PeriodicTable.equationCol, justify=tk.CENTER)]
            elif self._parent.eqMode() == 'forward':
                self._oldEqObjs = [self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = self._PeriodicTable.equationCol, width = 3)]
            elif self._parent.eqMode() == 'equilibrium':
                self._oldEqObjs = [self.create_line(x-30, y-4, x+30, y-4, x+24, y-8, x+24, y-4, fill = self._PeriodicTable.equationCol, width = 3, joinstyle=tk.MITER), self.create_line(x-24, y+4, x-24, y+8, x-30, y+4, x+30,y+4, fill = self._PeriodicTable.equationCol, width = 3, joinstyle=tk.MITER)]

    def fixEq(self, e: tk.Event) -> None:
        x, y = nearRound(e.x, 30), nearRound(e.y, 30)
        for i in self._oldEqObjs:
            self.delete(i)
        if self._parent.eqMode() == '+':
            self.create_text(x, y, text='+', font=('Helvetica','20','bold'), fill=self._PeriodicTable.equationCol, justify=tk.CENTER, tags=f"1 {self._PeriodicTable.equationCol.replace(' ', '_')} + {x} {y}")
        elif self._parent.eqMode() == 'forward':
            self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = self._PeriodicTable.equationCol, width = 3, tags=f"[0, 1, ({x}, {y})]")
        elif self._parent.eqMode() == 'equilibrium':
            self.create_line(x-30, y-4, x+30, y-4, x+24, y-8, x+24, y-4, fill = self._PeriodicTable.equationCol, width = 3, joinstyle=tk.MITER, tags=f"0 2 {x} {y}")
            self.create_line(x-24, y+4, x-24, y+8, x-30, y+4, x+30,y+4, fill = self._PeriodicTable.equationCol, width = 3, joinstyle=tk.MITER)
        self._eqObjCount += 1

    def makeLine(self, e: tk.Event) -> None:
        x, y = e.x, e.y
        if len(self._atomCenters) != 0:
            self._baseCoords = closestNode((x,y), self._atomCenters)
        else:
            self._baseCoords = x,y

    def drawLine(self, e: tk.Event) -> None:
        x, y = e.x, e.y
        x1, y1 = self._baseCoords
        rawangle = (180+math.degrees(math.pi-math.atan2((y-y1), (x-x1)))) % 360
        angle = math.radians(min([0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360], key=lambda x:abs(x-rawangle)))
        ex, ey = x1+(60*math.cos(angle)), y1+((60*math.sin(angle))*-1)
        line = self.create_line(ex, ey, x1, y1, width=2)
        if line != self._oldLine:
            self.delete(self._oldLine)
            self._oldLine = line

    def fixLine(self, e: tk.Event) -> None:
        x, y = e.x, e.y
        x1, y1 = self._baseCoords
        rawangle = (180+math.degrees(math.pi-math.atan2((y-y1), (x-x1)))) % 360
        angle = math.radians(min([0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360], key=lambda x:abs(x-rawangle)))
        fx, fy = nearRound((x1+(60*math.cos(angle))), 1), nearRound((y1+((60*math.sin(angle))*-1)), 1)
        sx, sy = x1+(15*math.cos(angle)), y1+((15*math.sin(angle))*-1)
        ex, ey = x1+(45*math.cos(angle)), y1+((45*math.sin(angle))*-1)
        bnum = int(self._parent.bondNo())
        mx, my = (5*math.cos(angle+(0.5*math.pi))), ((5*math.sin(angle+(0.5*math.pi)))*-1)
        lines = []
        if bnum % 2 == 1:
            lines = [(ex, ey, sx, sy)]
            for i in range((bnum-1)//2):
                i+=1
                lines.append((ex+(i*mx), ey+(i*my), sx+(i*mx), sy+(i*my)))
                lines.append((ex-(i*mx), ey-(i*my), sx-(i*mx), sy-(i*my)))        
        else:
            for i in range(bnum//2):
                i += 1
                lines.append((ex+((i-0.5)*mx), ey+((i-0.5)*my), sx+((i-0.5)*mx), sy+((i-0.5)*my)))
                lines.append((ex-((i-0.5)*mx), ey-((i-0.5)*my), sx-((i-0.5)*mx), sy-((i-0.5)*my))) 
        
        for x1, y1, x2, y2 in lines:
            self.create_line(x1, y1, x2, y2, width=2, tags=f"0 0 {x1} {y1} {x2} {y2}")

        if (fx, fy) not in self._atomCenters:
            self._bondEndsOpen.append((fx, fy))
        self.delete(self._oldLine)
        self._bondCount += 1
    
    def makeBrack(self, e: tk.Event) -> None:
        x, y = e.x, e.y
        if len(self._atomCenters) != 0:
            self._arcBaseCoords = closestNode((x,y), self._atomCenters)
        else:
            self._arcBaseCoords = x,y
        if self._parent._arcSide == 'right':
            self._oldArc = self.drawArc(self._arcBaseCoords, 60, (310, 100), 2, "")
        elif self._parent._arcSide == 'left':
            self._oldArc = self.drawArc(self._arcBaseCoords, 60, (130, 100), 2, "")
    
    def moveBrack(self, e: tk.Event) -> None:
        newCoords = closestNode((e.x,e.y), self._atomCenters)
        if newCoords != self._arcBaseCoords:
            self._arcBaseCoords = newCoords
            self.delete(self._oldArc)
            if self._parent._arcSide == 'right':
                self._oldArc = self.drawArc(self._arcBaseCoords, 60, (310, 100), 2, "")
            elif self._parent._arcSide == 'left':
                self._oldArc = self.drawArc(self._arcBaseCoords, 60, (130, 100), 2, "")
        
    def fixBrack(self, e: tk.Event) -> None:
        newCoords = closestNode((e.x,e.y), self._atomCenters)
        if newCoords != self._arcBaseCoords:
            self._arcBaseCoords = newCoords
        
        self.delete(self._oldArc)
        if self._parent._arcSide == 'right':
            self.drawArc(self._arcBaseCoords, 60, (310, 100), 2, f"2 1 {self._arcBaseCoords[0]} {self._arcBaseCoords[0]}")
            self.create_text(self._arcBaseCoords[0]+25, self._arcBaseCoords[1]+50, text="n", font=('Helvetica','11','bold'), fill="black", justify=tk.CENTER)
        elif self._parent._arcSide == 'left':
            self.drawArc(self._arcBaseCoords, 60, (130, 100), 2, f"2 0 {self._arcBaseCoords[0]} {self._arcBaseCoords[0]}")
        
        
    def clearAll(self) -> None:
        check = tk.messagebox.askquestion('Clear Canvas', 'Are you sure you want to clear the canvas?', icon='warning')
        if check == 'yes':
            self.delete('all')
            self.stateClear()
