from src._classes import TopLevel, Canvas, Frame
from PIL import Image, ImageChops, ImageDraw
import tkinter as tk
import time
import os

class ImageWindow(TopLevel):
    def __init__(self, parent, info, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.geometry('1280x720')
        self.title('Image Generator')

        self.xVal = tk.DoubleVar(value='2000')
        self.yVal = tk.DoubleVar(value='2000')

        self.imageFrame = ImageCanvas(self,  bd=1, relief=tk.RAISED)
        self.imageFrame.pack(side = tk.TOP, fill=tk.BOTH, padx = 8, pady = (8, 4), expand=True)
        self.imageFrame.addObjs(info)  

        self.optionFrame = OptionFrame(self, bd=1, relief=tk.RAISED)
        self.optionFrame.pack(side=tk.BOTTOM, padx=8, pady=(4, 8), ipadx=5, ipady=5, fill=tk.X)

    def makeImage(self) -> None:
        self.imageFrame.saveImage(self.xVal, self.yVal)
        self.imageFrame.pack_forget()
        del self.imageFrame
        self.destroy()
    
    def getY(self) -> int:
        return self.yVal
    
    def getX(self) -> int:
        return self.xVal


class PixelFrame(Frame):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        tk.Label(self, text="Image Format", font=('Helvetica', '11','bold')).pack(side=tk.LEFT)
        tk.Label(self, text="x: ", font=('Helvetica', '11')).pack(side=tk.LEFT)
        
        self.xInput = tk.Spinbox(self, textvariable=self._parent.parent().getX())
        self.xInput.pack(side=tk.LEFT)

        tk.Label(self, text="y: ", font=('Helvetica', '11')).pack(side=tk.LEFT)

        self.yInput = tk.Spinbox(self, textvariable=self._parent.parent().getY())
        self.yInput.pack(side=tk.LEFT)


class OptionFrame(Frame):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.pixelMenu = PixelFrame(self, bd=1, relief=tk.RAISED)
        self.pixelMenu.pack(side = tk.LEFT, padx = (8, 4), pady=8, fill=tk.X)

        self.button = tk.Button(self, text="Save Image", relief=tk.RAISED, bg='gray', command= lambda: self._parent.makeImage())
        self.button.pack(side=tk.BOTTOM, padx=(4, 8), pady=8, fill=tk.X)


class ImageCanvas(Canvas):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
    def addObjs(self, info) -> None:
        for obj in info:
            if int(obj[0]) == 0:
                self.addLine(obj)
            elif int(obj[0]) == 1:
                self.addText(obj[2], obj[1].replace('_', ' '), float(obj[3]), float(obj[4]))
            elif int(obj[0]) == 2:
                self.addBrackets(int(obj[1]), int(obj[2]), int(obj[3]))

    def addLine(self, obj) -> None:
        if int(obj[1]) == 0:
            self.addBond(float(obj[2]), float(obj[3]), float(obj[4]), float(obj[5]))
        elif int(obj[1]) == 1:
            self.addForward(float(obj[2]), float(obj[3]))
        elif int(obj[1]) == 2:
            self.addEquilib(float(obj[2]), float(obj[3]))

    def addBond(self, x1: float | int, y1: float | int, x2: float | int, y2: float | int) -> None:
        self.create_line(x1, y1, x2, y2, width=2)

    def addForward(self, x: float | int, y: float | int) -> None:
        self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = 'dark green', width = 5)

    def addEquilib(self, x: float | int, y: float | int) -> None:
        self.create_line(x-30, y-6, x+30, y-6, x+24, y-12, x+24, y-6, fill = 'dark green', width = 5, joinstyle=tk.MITER)
        self.create_line(x-24, y+6, x-24, y+12, x-30, y+6, x+30,y+6, fill = 'dark green', width = 5, joinstyle=tk.MITER)

    def addText(self, txt: str, colour: str, x: float | int, y: float | int) -> None:
        self.create_text(x, y, text=txt, font=('Helvetica','18','bold'), fill=colour, justify=tk.CENTER)

    def addBrackets(self, type: int, x: float | int, y: float | int) -> None:
        if type == 1:
            self.drawArc((x, y), 60, (310, 100), 2, "")
        elif type == 0:
            self.drawArc((x, y), 60, (130, 100), 2, "")
        
    def saveImage(self, width, height) -> None:
        pwd = os.path.dirname(os.path.realpath(__file__))
        self.postscript(file = pwd+'\\temp.eps', colormode='color', pagewidth=width, pageheight=height) 
        img = Image.open(pwd+'\\temp.eps') 
        ma, mi = img.size
        bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            trimb = (max(bbox[0]-5, 0), max(bbox[1]-5, 0), min(bbox[2]+5, ma), min(bbox[3]+5, ma))
            print(trimb)
            img = img.crop(trimb)
            img.show()
        os.remove(pwd+'\\temp.eps')