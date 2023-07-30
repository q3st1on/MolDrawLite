import tkinter as tk
from tkinter import ttk
from src._classes import Frame, ButtonCanvas

class SideMenu(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.mb = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.mb.pack(side = tk.TOP, pady=(5, 0))
        self.mb.create_line(5,12.5,21.5,12.5, width=2)
        self.mb.bind('<Button-1>', lambda _: self._parent.setBond(1))

        self.eb = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.eb.pack(side = tk.TOP)

        self.eb.create_line(5,10.5,21.5,10.5, width=2)
        self.eb.create_line(5,13.5,21.5,13.5, width=2)
        self.eb.bind('<Button-1>', lambda _: self._parent.setBond(2))

        self.pb = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.pb.pack(side = tk.TOP)

        self.pb.create_line(5,9.5,21.5,9.5, width=2)
        self.pb.create_line(5,12.5,21.5,12.5, width=2)
        self.pb.create_line(5,15.5,21.5,15.5, width=2)
        self.pb.bind('<Button-1>', lambda _: self._parent.setBond(3))

        self.bb = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.bb.pack(side = tk.TOP)

        self.bb.create_line(5,7.5,21.5,7.5, width=2)
        self.bb.create_line(5,10.5,21.5,10.5, width=2)
        self.bb.create_line(5,13.5,21.5,13.5, width=2)
        self.bb.create_line(5,16.5,21.5,16.5, width=2)
        self.bb.bind('<Button-1>', lambda _: self._parent.setBond(4))

        self.qb = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.qb.pack(side = tk.TOP, pady=(0, 5))

        self.qb.create_line(5,6.5,21.5,6.5, width=2)
        self.qb.create_line(5,9.5,21.5,9.5, width=2)
        self.qb.create_line(5,12.5,21.5,12.5, width=2)
        self.qb.create_line(5,15.5,21.5,15.5, width=2)
        self.qb.create_line(5,18.5,21.5,18.5, width=2)
        self.qb.bind('<Button-1>', lambda _: self._parent.setBond(5))

        ttk.Separator(self, orient='horizontal').pack(fill = 'x')

        self.hydrogen = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.hydrogen.pack(side=tk.TOP, pady=(5, 0))
        self.hydrogen.bind('<Button-1>', (lambda _: self._parent.setAtom(1)))
        self.hydrogenS = self.hydrogen.create_text(11, 11, text='H', font=('Helvetica','18','bold'), fill = self._PeriodicTable.atomNo(1).colour, tags='atom')
        self.hydrogen.moveItem(self.hydrogenS, self.hydrogen.findCenter(self.hydrogenS))
        
        self.carbon = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg = 'gray')
        self.carbon.pack(side=tk.TOP)
        self.carbon.bind('<Button-1>', (lambda _: self._parent.setAtom(6)))
        self.carbonS = self.carbon.create_text(11, 11,anchor=tk.CENTER, text='C', font=('Helvetica','18','bold'), fill = self._PeriodicTable.atomNo(6).colour, tags='atom', justify=tk.CENTER)
        self.carbon.moveItem(self.carbonS, self.carbon.findCenter(self.carbonS))

        self.nitrogen = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.nitrogen.pack(side=tk.TOP)
        self.nitrogen.bind('<Button-1>', (lambda _: self._parent.setAtom(7)))
        self.nitrogenS = self.nitrogen.create_text(11, 11, text='N', font=('Helvetica','18','bold'), fill = self._PeriodicTable.atomNo(7).colour, tags='atom')
        self.nitrogen.moveItem(self.nitrogenS, self.nitrogen.findCenter(self.nitrogenS))

        self.oxygen = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.oxygen.pack(side=tk.TOP)
        self.oxygen.bind('<Button-1>', (lambda _: self._parent.setAtom(8)))
        self.oxygenS = self.oxygen.create_text(11, 11, text='O', font=('Helvetica','18','bold'), fill = self._PeriodicTable.atomNo(8).colour, tags='atom')
        self.oxygen.moveItem(self.oxygenS, self.oxygen.findCenter(self.oxygenS))

        self.R = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.R.pack(side=tk.TOP)
        self.R.bind('<Button-1>', (lambda _: self._parent.setAtom(0)))
        self.RS = self.R.create_text(11, 11, text='R', font=('Helvetica','18','bold'), fill = self._PeriodicTable.atomNo(0).colour, tags='atom')
        self.R.moveItem(self.RS, self.R.findCenter(self.RS))

        self.menu = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.menu.pack(side=tk.TOP)
        self.menu.bind('<Button-1>', (lambda _: self._parent.createTable('picker')))
        self.menuS = self.menu.create_text(11, 11, text='#', font=('Helvetica','18','bold'), fill = 'black', tags='atom')
        self.menu.moveItem(self.menuS, self.menu.findCenter(self.menuS))


        self.elementFrame = tk.Frame(self, width=21, height=21)
        self.elementFrame.pack(side=tk.TOP, pady = (0, 5))
        self.element = tk.Label(self.elementFrame, textvariable=self._parent.element)
        self.element.pack()

        ttk.Separator(self, orient='horizontal').pack(fill = 'x')

        self.ep = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.ep.pack(side = tk.TOP, pady=(5, 0))
        self.eps = self.ep.create_text(11, 11, text='+', font=('Helvetica','18','bold'), fill = self._PeriodicTable.equationCol)
        self.ep.bind('<Button-1>', lambda _: self._parent.setSymbol('+'))
        self.ep.moveItem(self.eps, self.ep.findCenter(self.eps))

        self.ef = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.ef.pack(side = tk.TOP)
        self.ef.create_line(5,12.5,20.5,12.5, width=2, arrow=tk.LAST, fill=self._PeriodicTable.equationCol)
        self.ef.bind('<Button-1>', lambda _: self._parent.setSymbol('forward'))

        self.ee = ButtonCanvas(self, relief=tk.RAISED, bd=1, width=21, height=21, bg='light gray')
        self.ee.pack(side = tk.TOP, pady=(0, 5))
        self.ee.create_line(5,10.5,21.5,10.5, 18, 8.5, width=2, fill = self._PeriodicTable.equationCol, joinstyle=tk.MITER)
        self.ee.create_line(6, 15.5, 5,13.5,21.5,13.5, width=2, fill = self._PeriodicTable.equationCol, joinstyle=tk.MITER)
        self.ee.bind('<Button-1>', lambda _: self._parent.setSymbol('equilibrium'))

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
                self.R.itemconfig(self.RS, fill=self._PeriodicTable.atomNo(0).colour)
            case 1:
                self.hydrogen.itemconfig(self.hydrogenS, fill=self._PeriodicTable.atomNo(1).colour)
            case 6:
                self.carbon.itemconfig(self.carbonS, fill=self._PeriodicTable.atomNo(6).colour)
            case 7:
                self.nitrogen.itemconfig(self.nitrogenS, fill=self._PeriodicTable.atomNo(7).colour)
            case 8:
                self.oxygen.itemconfig(self.oxygenS, fill=self._PeriodicTable.atomNo(8).colour)

    def updateEqButtons(self):
        self.ep.itemconfig('all', fill = self._PeriodicTable.equationCol)
        self.ef.itemconfig('all', fill = self._PeriodicTable.equationCol)
        self.ee.itemconfig('all', fill = self._PeriodicTable.equationCol)


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