from PIL import Image, ImageChops
import tkinter as tk
import time
import os

class imageWindow(tk.Toplevel):
    def __init__(self, parent, info, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.geometry('1280x720')
        self.title('Image Generator')

        self.xVal = tk.DoubleVar(value='2000')
        self.yVal = tk.DoubleVar(value='2000')

        self.imageFrame = imageCanvas(self,  bd=1, relief=tk.RAISED)
        self.imageFrame.pack(side = tk.TOP, fill=tk.BOTH, padx = 8, pady = (8, 4), expand=True)
        self.imageFrame.addObjs(info)  

        self.optionFrame = optionFrame(self, bd=1, relief=tk.RAISED)
        self.optionFrame.pack(side=tk.BOTTOM, padx=8, pady=(4, 8), ipadx=5, ipady=5, fill=tk.X)

    def makeImage(self):
        self.imageFrame.test(self.xVal, self.yVal)
        time.sleep(60)
        self.imageFrame.saveImage()
        self.imageFrame.pack_forget()
        del self.imageFrame
        self.destroy()
    
    def getParent(self):
        return self.parent
    
    def getY(self):
        return self.yVal
    
    def getX(self):
        return self.xVal


class pixelFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self, text="Image Format", font=('Helvetica', '11','bold')).pack(side=tk.LEFT)
        tk.Label(self, text="x: ", font=('Helvetica', '11')).pack(side=tk.LEFT)
        
        self.xInput = tk.Spinbox(self, textvariable=self.parent.getParent().getX())
        self.xInput.pack(side=tk.LEFT)

        tk.Label(self, text="y: ", font=('Helvetica', '11')).pack(side=tk.LEFT)

        self.yInput = tk.Spinbox(self, textvariable=self.parent.getParent().getY())
        self.yInput.pack(side=tk.LEFT)
    
    def getParent(self):
        return self.parent


class optionFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.pixelMenu = pixelFrame(self, bd=1, relief=tk.RAISED)
        self.pixelMenu.pack(side = tk.LEFT, padx = (8, 4), pady=8, fill=tk.X)

        self.button = tk.Button(self, text="Save Image", relief=tk.RAISED, bg='gray', command= lambda: self.parent.makeImage())
        self.button.pack(side=tk.BOTTOM, padx=(4, 8), pady=8, fill=tk.X)
    
    def getParent(self):
        return self.parent


class imageCanvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    def addObjs(self, info):
        for obj in info:
            if int(obj[0]) == 0:
                self.addLine(obj)
            elif int(obj[0]) == 1:
                self.addText(obj[2], obj[1], float(obj[3]), float(obj[4]))

    def addLine(self, obj):
        if int(obj[1]) == 0:
            self.addBond(float(obj[2]), float(obj[3]), float(obj[4]), float(obj[5]))
        elif int(obj[1]) == 1:
            self.addForward(float(obj[2]), float(obj[3]))
        elif int(obj[1]) == 2:
            self.addEquilib(float(obj[2]), float(obj[3]))

    def addBond(self, x1, y1, x2, y2):
        self.create_line(x1, y1, x2, y2, width=2)

    def addForward(self, x, y):
        self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = 'dark green', width = 5)

    def addEquilib(self, x, y):
        self.create_line(x-30, y-6, x+30, y-6, x+24, y-12, x+24, y-6, fill = 'dark green', width = 5, joinstyle=tk.MITER)
        self.create_line(x-24, y+6, x-24, y+12, x-30, y+6, x+30,y+6, fill = 'dark green', width = 5, joinstyle=tk.MITER)

    def addText(self, txt, colour, x, y):
        print(f"{x}, {y}")
        self.create_text(x, y, text=txt, font=('Helvetica','18','bold'), fill=colour, justify=tk.CENTER)
    
    def test(self, width, height):
        self.postscript(file = 'temp.eps', colormode='color', pagewidth=width, pageheight=height) 
    # def saveImage(self, width, height):
        # self.postscript(file = 'temp.eps', colormode='color', pagewidth=width, pageheight=height) 
    def saveImage(self):
        print('eps')
        img = Image.open('temp.eps') 
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
        os.remove('temp.eps')
    
    def getParent(self):
        return self.parent
