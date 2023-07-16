import tkinter as tk
from tkinter import ttk

class sideMenu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.mb = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.mb.pack(side = tk.TOP, pady=(5, 0))

        self.mb.create_line(4,11,20,11, width=2)
        self.mb.bind('<Button-1>', lambda _: self.parent.setBond(1))

        self.eb = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.eb.pack(side = tk.TOP)

        self.eb.create_line(4,10,20,10, width=2)
        self.eb.create_line(4,13,20,13, width=2)
        self.eb.bind('<Button-1>', lambda _: self.parent.setBond(2))

        self.pb = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.pb.pack(side = tk.TOP)

        self.pb.create_line(4,9,20,9, width=2)
        self.pb.create_line(4,12,20,12, width=2)
        self.pb.create_line(4,15,20,15, width=2)
        self.pb.bind('<Button-1>', lambda _: self.parent.setBond(3))

        self.bb = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.bb.pack(side = tk.TOP)

        self.bb.create_line(4,7,20,7, width=2)
        self.bb.create_line(4,10,20,10, width=2)
        self.bb.create_line(4,13,20,13, width=2)
        self.bb.create_line(4,16,20,16, width=2)
        self.bb.bind('<Button-1>', lambda _: self.parent.setBond(4))

        self.qb = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.qb.pack(side = tk.TOP, pady=(0, 5))

        self.qb.create_line(4,6,20,6, width=2)
        self.qb.create_line(4,9,20,9, width=2)
        self.qb.create_line(4,12,20,12, width=2)
        self.qb.create_line(4,15,20,15, width=2)
        self.qb.create_line(4,18,20,18, width=2)
        self.qb.bind('<Button-1>', lambda _: self.parent.setBond(5))

        ttk.Separator(self, orient='horizontal').pack(fill = 'x')

        self.hydrogen = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.hydrogen.pack(side=tk.TOP, pady=(5, 0))
        self.hydrogen.bind('<Button-1>', (lambda _: self.parent.setAtom(1)))
        self.hydrogen.create_text(12, 15, text='H', font=('Helvetica','18','bold'), fill = 'gray45')

        self.carbon = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg = 'gray')
        self.carbon.pack(side=tk.TOP)
        self.carbon.bind('<Button-1>', (lambda _: self.parent.setAtom(6)))
        self.carbon.create_text(12, 15, text='C', font=('Helvetica','18','bold'), fill = 'gray11')

        self.nitrogen = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.nitrogen.pack(side=tk.TOP)
        self.nitrogen.bind('<Button-1>', (lambda _: self.parent.setAtom(7)))
        self.nitrogen.create_text(12, 15, text='N', font=('Helvetica','18','bold'), fill = 'deep sky blue')

        self.oxygen = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.oxygen.pack(side=tk.TOP)
        self.oxygen.bind('<Button-1>', (lambda _: self.parent.setAtom(8)))
        self.oxygen.create_text(12, 15, text='O', font=('Helvetica','18','bold'), fill = 'red2')

        self.elementFrame = tk.Frame(self, width=20, height=20)
        self.elementFrame.pack(side=tk.TOP, pady = (0, 5))
        self.element = tk.Label(self.elementFrame, textvariable=self.parent.getElement())
        self.element.pack()

        ttk.Separator(self, orient='horizontal').pack(fill = 'x')

        self.ep = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.ep.pack(side = tk.TOP, pady=(5, 0))
        self.ep.create_text(12, 12, text='+', font=('Helvetica','18','bold'), fill = 'dark green')
        self.ep.bind('<Button-1>', lambda _: self.parent.setSymbol('+'))

        self.ef = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.ef.pack(side = tk.TOP)
        self.ef.create_line(4,12,20,12, width=2, arrow=tk.LAST, fill='dark green')
        self.ef.bind('<Button-1>', lambda _: self.parent.setSymbol('forward'))

        self.ee = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.ee.pack(side = tk.TOP, pady=(0, 5))
        self.ee.create_line(4,10,20,10, 18, 8, width=2, fill = 'dark green', joinstyle=tk.MITER)
        self.ee.create_line(6, 15, 4,13,20,13, width=2, fill = 'dark green', joinstyle=tk.MITER)
        self.ee.bind('<Button-1>', lambda _: self.parent.setSymbol('equilibrium'))

        ttk.Separator(self, orient='horizontal').pack(fill = 'x')


    def updateElemHighlight(self, elem):
        elem = int(elem)
        match elem:
            case 1:
                self.hydrogen.configure(bg='gray')
                self.carbon.configure(bg='light gray')
                self.nitrogen.configure(bg='light gray')
                self.oxygen.configure(bg='light gray')
            case 6:
                self.hydrogen.configure(bg='light gray')
                self.carbon.configure(bg='gray')
                self.nitrogen.configure(bg='light gray')
                self.oxygen.configure(bg='light gray')
            case 7:
                self.hydrogen.configure(bg='light gray')
                self.carbon.configure(bg='light gray')
                self.nitrogen.configure(bg='gray')
                self.oxygen.configure(bg='light gray')
            case 8:
                self.hydrogen.configure(bg='light gray')
                self.carbon.configure(bg='light gray')
                self.nitrogen.configure(bg='light gray')
                self.oxygen.configure(bg='gray')
            case _:
                self.deacElem()

    def deacElem(self):
        self.hydrogen.configure(bg='light gray')
        self.carbon.configure(bg='light gray')
        self.nitrogen.configure(bg='light gray')
        self.oxygen.configure(bg='light gray')

    def updateSymbol(self, x):
        match x:
            case '+':
                self.ep.configure(bg='gray')
                self.ef.configure(bg='light gray')
                self.ee.configure(bg='light gray')
            case 'forward':
                self.ep.configure(bg='light gray')
                self.ef.configure(bg='gray')
                self.ee.configure(bg='light gray')
            case 'equilibrium':
                self.ep.configure(bg='light gray')
                self.ef.configure(bg='light gray')
                self.ee.configure(bg='gray')
            case _:
                pass
    
    def deacSymbol(self):
        self.ep.configure(bg='light gray')
        self.ef.configure(bg='light gray')
        self.ee.configure(bg='light gray')

    def updateBond(self, num):
        match num:
            case 1:
                self.mb.configure(bg='gray')
                self.eb.configure(bg='light gray')
                self.pb.configure(bg='light gray')
                self.bb.configure(bg='light gray')
                self.qb.configure(bg='light gray')
            case 2:
                self.mb.configure(bg='light gray')
                self.eb.configure(bg='gray')
                self.pb.configure(bg='light gray')
                self.bb.configure(bg='light gray')
                self.qb.configure(bg='light gray')
            case 3:
                self.mb.configure(bg='light gray')
                self.eb.configure(bg='light gray')
                self.pb.configure(bg='gray')
                self.bb.configure(bg='light gray')
                self.qb.configure(bg='light gray')
            case 4:
                self.mb.configure(bg='light gray')
                self.eb.configure(bg='light gray')
                self.pb.configure(bg='light gray')
                self.bb.configure(bg='gray')
                self.qb.configure(bg='light gray')
            case 5:
                self.mb.configure(bg='light gray')
                self.eb.configure(bg='light gray')
                self.pb.configure(bg='light gray')
                self.bb.configure(bg='light gray')
                self.qb.configure(bg='gray')
            case _:
                pass

    def deacBond(self):
        self.mb.configure(bg='light gray')
        self.eb.configure(bg='light gray')
        self.pb.configure(bg='light gray')
        self.bb.configure(bg='light gray')
        self.qb.configure(bg='light gray')
    
    def getParent(self):
        return self.parent
