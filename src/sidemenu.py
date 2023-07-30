import tkinter as tk
from tkinter import ttk
from src.atomDicts import PeriodicTable

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
        self.hydrogenS = self.hydrogen.create_text(12, 15, text='H', font=('Helvetica','18','bold'), fill = PeriodicTable.atomNo(1).colour, tags='atom')

        self.carbon = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg = 'gray')
        self.carbon.pack(side=tk.TOP)
        self.carbon.bind('<Button-1>', (lambda _: self.parent.setAtom(6)))
        self.carbonS = self.carbon.create_text(12, 15, text='C', font=('Helvetica','18','bold'), fill = PeriodicTable.atomNo(6).colour, tags='atom')

        self.nitrogen = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.nitrogen.pack(side=tk.TOP)
        self.nitrogen.bind('<Button-1>', (lambda _: self.parent.setAtom(7)))
        self.nitrogenS = self.nitrogen.create_text(12, 15, text='N', font=('Helvetica','18','bold'), fill = PeriodicTable.atomNo(7).colour, tags='atom')

        self.oxygen = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.oxygen.pack(side=tk.TOP)
        self.oxygen.bind('<Button-1>', (lambda _: self.parent.setAtom(8)))
        self.oxygenS = self.oxygen.create_text(12, 15, text='O', font=('Helvetica','18','bold'), fill = PeriodicTable.atomNo(8).colour, tags='atom')

        self.R = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.R.pack(side=tk.TOP)
        self.R.bind('<Button-1>', (lambda _: self.parent.setAtom(0)))
        self.RS = self.R.create_text(12, 15, text='R', font=('Helvetica','18','bold'), fill = PeriodicTable.atomNo(0).colour, tags='atom')

        self.menu = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.menu.pack(side=tk.TOP)
        self.menu.bind('<Button-1>', (lambda _: self.parent.createTable('picker')))
        self.menu.create_text(12, 15, text='#', font=('Helvetica','18','bold'), fill = 'black', tags='atom')

        self.elementFrame = tk.Frame(self, width=20, height=20)
        self.elementFrame.pack(side=tk.TOP, pady = (0, 5))
        self.element = tk.Label(self.elementFrame, textvariable=self.parent.element)
        self.element.pack()

        ttk.Separator(self, orient='horizontal').pack(fill = 'x')

        self.ep = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.ep.pack(side = tk.TOP, pady=(5, 0))
        self.ep.create_text(12, 12, text='+', font=('Helvetica','18','bold'), fill = PeriodicTable.equationCol)
        self.ep.bind('<Button-1>', lambda _: self.parent.setSymbol('+'))

        self.ef = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.ef.pack(side = tk.TOP)
        self.ef.create_line(4,12,20,12, width=2, arrow=tk.LAST, fill=PeriodicTable.equationCol)
        self.ef.bind('<Button-1>', lambda _: self.parent.setSymbol('forward'))

        self.ee = tk.Canvas(self, relief=tk.RAISED, bd=1, width=20, height=20, bg='light gray')
        self.ee.pack(side = tk.TOP, pady=(0, 5))
        self.ee.create_line(4,10,20,10, 18, 8, width=2, fill = PeriodicTable.equationCol, joinstyle=tk.MITER)
        self.ee.create_line(6, 15, 4,13,20,13, width=2, fill = PeriodicTable.equationCol, joinstyle=tk.MITER)
        self.ee.bind('<Button-1>', lambda _: self.parent.setSymbol('equilibrium'))

        ttk.Separator(self, orient='horizontal').pack(fill = 'x')


    def updateElemHighlight(self, elem):
        match elem:
            case 0:
                self.R.configure(bg='gray')
                self.hydrogen.configure(bg='light gray')
                self.carbon.configure(bg='light gray')
                self.nitrogen.configure(bg='light gray')
                self.oxygen.configure(bg='light gray')
            case 1:
                self.R.configure(bg='light gray')
                self.hydrogen.configure(bg='gray')
                self.carbon.configure(bg='light gray')
                self.nitrogen.configure(bg='light gray')
                self.oxygen.configure(bg='light gray')
            case 6:
                self.R.configure(bg='light gray')
                self.hydrogen.configure(bg='light gray')
                self.carbon.configure(bg='gray')
                self.nitrogen.configure(bg='light gray')
                self.oxygen.configure(bg='light gray')
            case 7:
                self.R.configure(bg='light gray')
                self.hydrogen.configure(bg='light gray')
                self.carbon.configure(bg='light gray')
                self.nitrogen.configure(bg='gray')
                self.oxygen.configure(bg='light gray')
            case 8:
                self.R.configure(bg='light gray')
                self.hydrogen.configure(bg='light gray')
                self.carbon.configure(bg='light gray')
                self.nitrogen.configure(bg='light gray')
                self.oxygen.configure(bg='gray')
            case _:
                self.deacElem()
    
    def updateElemButtons(self, elem):
        match elem:
            case 0:
                self.R.itemconfig(self.RS, fill=PeriodicTable.atomNo(0).colour)
            case 1:
                self.hydrogen.itemconfig(self.hydrogenS, fill=PeriodicTable.atomNo(1).colour)
            case 6:
                self.carbon.itemconfig(self.carbonS, fill=PeriodicTable.atomNo(6).colour)
            case 7:
                self.nitrogen.itemconfig(self.nitrogenS, fill=PeriodicTable.atomNo(7).colour)
            case 8:
                self.oxygen.itemconfig(self.oxygenS, fill=PeriodicTable.atomNo(8).colour)

    def updateEqButtons(self):
        self.ep.itemconfig('all', fill = PeriodicTable.equationCol)
        self.ef.itemconfig('all', fill = PeriodicTable.equationCol)
        self.ee.itemconfig('all', fill = PeriodicTable.equationCol)


    def deacElem(self):
        self.R.configure(bg='light gray')
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
