from src.util import myround, closest_node
import math
import tkinter as tk

class genCanvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.bind('<Button-1>', self.parent.mousedown)
        self.bind('<B1-Motion>', self.parent.mousemove)
        self.bind('<ButtonRelease-1>', self.parent.mouseup)

    def make_letter(self, e):
        x, y = e.x, e.y
        rx, ry = myround(e.x, 60), myround(e.y, 60)
        if len(self.parent.bondendsopen) != 0:
            self.parent.old_letter_coords = closest_node((x,y), self.parent.bondendsopen+[(rx, ry)])
        else:
            self.parent.old_letter_coords = rx,ry
        x,y = self.parent.old_letter_coords
        self.parent.old_letter = self.create_text(x, y+3, text=self.parent.selectedelem(), font=('Helvetica','18','bold'), fill=self.parent.elemcolour(), justify=tk.CENTER)

    def move_letter(self, e):
        x, y = e.x, e.y
        rx, ry = myround(e.x, 60), myround(e.y, 60)
        x1, y1 = self.parent.old_letter_coords
        if (x,y) != (x1, y1):
            if len(self.parent.bondendsopen) != 0:
                self.parent.old_letter_coords = closest_node((x,y), self.parent.bondendsopen+[(rx, ry)])
            else:
                self.parent.old_letter_coords = rx,ry
            self.delete(self.parent.old_letter)
        x,y = self.parent.old_letter_coords
        self.parent.old_letter = self.create_text(x, y+3, text=self.parent.selectedelem(), font=('Helvetica','18','bold'), fill=self.parent.elemcolour(), justify=tk.CENTER)

    def fix_letter(self, e):
        x, y = self.parent.old_letter_coords
        self.delete(self.parent.old_letter)
        self.create_text(x, y+3, text=self.parent.selectedelem(), font=('Helvetica','18','bold'), fill=self.parent.elemcolour(), justify=tk.CENTER, tags=f"1 {self.parent.elemcolour()} {self.parent.selectedelem()} {x} {y}")
        self.parent.atomcenters.append((x,y))
        if self.parent.old_letter_coords in self.parent.bondendsopen:
            self.parent.bondendsopen.remove(self.parent.old_letter_coords)
        self.parent.atomcount += 1

    def makeeq(self, e):
        x, y = myround(e.x, 60), myround(e.y, 60)
        self.parent.old_eq_coords = x, y
        if self.parent.eqmode == '+':
            self.parent.old_eq_objs = [self.create_text(x, y-1, text='+', font=('Helvetica','30','bold'), fill='dark green', justify=tk.CENTER)]
        elif self.parent.eqmode == 'forward':
            self.parent.old_eq_objs = [self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = 'dark green', width = 5)]
        elif self.parent.eqmode == 'equilibrium':
            self.parent.old_eq_objs = [self.create_line(x-30, y-6, x+30, y-6, x+24, y-12, x+24, y-6, fill = 'dark green', width = 5, joinstyle=tk.MITER), self.create_line(x-24, y+6, x-24, y+12, x-30, y+6, x+30,y+6, fill = 'dark green', width = 5, joinstyle=tk.MITER)]

    def moveeq(self, e):
        x, y = myround(e.x, 60), myround(e.y, 60)
        if self.parent.old_eq_coords != (x, y):
            self.parent.old_eq_coords = (x, y)
            for i in self.parent.old_eq_objs:
                self.delete(i)
            if self.parent.eqmode == '+':
                self.parent.old_eq_objs = [self.create_text(x, y-1, text='+', font=('Helvetica','30','bold'), fill='dark green', justify=tk.CENTER)]
            elif self.parent.eqmode == 'forward':
                self.parent.old_eq_objs = [self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = 'dark green', width = 5)]
            elif self.parent.eqmode == 'equilibrium':
                self.parent.old_eq_objs = [self.create_line(x-30, y-6, x+30, y-6, x+24, y-12, x+24, y-6, fill = 'dark green', width = 5, joinstyle=tk.MITER), self.create_line(x-24, y+6, x-24, y+12, x-30, y+6, x+30,y+6, fill = 'dark green', width = 5, joinstyle=tk.MITER)]

    def fix_eq(self, e):
        x, y = myround(e.x, 60), myround(e.y, 60)
        for i in self.parent.old_eq_objs:
            self.delete(i)
        if self.parent.eqmode == '+':
            self.create_text(x, y-1, text='+', font=('Helvetica','30','bold'), fill='dark green', justify=tk.CENTER, tags=f"1 dark\ green + {x} {y}")
        elif self.parent.eqmode == 'forward':
            self.create_line(x-30, y, x+30, y, arrow=tk.LAST, fill = 'dark green', width = 5, tags=f"[0, 1, ({x}, {y})]")
        elif self.parent.eqmode == 'equilibrium':
            self.create_line(x-30, y-6, x+30, y-6, x+24, y-12, x+24, y-6, fill = 'dark green', width = 5, joinstyle=tk.MITER, tags=f"0 2 {x} {y}")
            self.create_line(x-24, y+6, x-24, y+12, x-30, y+6, x+30,y+6, fill = 'dark green', width = 5, joinstyle=tk.MITER)
        self.parent.eqobcount += 1

    def make_line(self, e):
        x, y = e.x, e.y
        if len(self.parent.atomcenters) != 0:
            self.parent.base_coords = closest_node((x,y), self.parent.atomcenters)
        else:
            self.parent.base_coords = x,y

    def draw_line(self, e):
        x, y = e.x, e.y
        x1, y1 = self.parent.base_coords
        rawangle = (180+math.degrees(math.pi-math.atan2((y-y1), (x-x1)))) % 360
        angle = math.radians(min([0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360], key=lambda x:abs(x-rawangle)))
        ex, ey = x1+(60*math.cos(angle)), y1+((60*math.sin(angle))*-1)
        line = self.create_line(ex, ey, x1, y1, width=2)
        if line != self.parent.old_line:
            self.delete(self.parent.old_line)
            self.parent.old_line = line

    def fix_line(self, e):
        x, y = e.x, e.y
        x1, y1 = self.parent.base_coords
        rawangle = (180+math.degrees(math.pi-math.atan2((y-y1), (x-x1)))) % 360
        angle = math.radians(min([0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360], key=lambda x:abs(x-rawangle)))
        fx, fy = myround((x1+(60*math.cos(angle))), 1), myround((y1+((60*math.sin(angle))*-1)), 1)
        sx, sy = x1+(15*math.cos(angle)), y1+((15*math.sin(angle))*-1)
        ex, ey = x1+(45*math.cos(angle)), y1+((45*math.sin(angle))*-1)
        bnum = int(self.parent.bondno)
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

        if (fx, fy) not in self.parent.atomcenters:
            self.parent.bondendsopen.append((fx, fy))
        self.delete(self.parent.old_line)
        self.parent.bondcount += 1
    
    def getParent(self):
        return self.parent
