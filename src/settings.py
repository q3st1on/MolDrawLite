import tkinter as tk

class createCFG(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title('Settings')

        self.needed = {'1': 'keycode', '2': 'keycode', '3': 'keycode', '4': 'keycode', '5': 'keycode', 'c': 'keycode', 'h': 'keycode', 'n': 'keycode', 'o': 'keycode', 'r': 'keycode', '+': 'keysym_num', '=': 'keysym_num', '>': 'keysym_num', 'b': 'keysym_num', 'a': 'keysym_num', 'e': 'keysym_num', 'shift+b': 'keysym_num', 'shift+a': 'keysym_num', 'shift+e': 'keysym_num', 'backspace': 'keycode', 'delete': 'keycode', 'enter': 'keysym_num'}
        self.keys = ["1","2","3","4","5","c","h","n","o","r","=",">","b","a","e","backspace","delete","enter","shift+b","shift+a","shift+e","+"]

        self.i = 0
        self.shift=True
        self.current = self.keys[self.i]
        self.cfg={}

        self.textVar = tk.StringVar()
        self.textVar.set("Please press key: "+str(self.current))

        self.message = tk.Label(self, textvariable=self.textVar, relief=tk.RAISED)
        self.message.pack() 

        self.bind("<KeyPress>", lambda x: self.keydown(x))

    def keydown(self, e):
        if self.current=="shift+b" & self.shift:
            self.textVar.set("Please press and hold the shift key for the rest of this keymapping")
        else:
            if self.needed[self.current] == 'keycode':
                self.cfg[self.current] = e.keycode
            elif self.needed[self.current] == 'keysym_num':
                self.cfg[self.current] == e.keysym_num
            elif self.current!="+"
                self.i = self.i+1
                self.current = self.keys[self.i]
                self.textVar.set("Please press key: "+str(self.current))
            else:
                self.destroy()

    def kill(self):
        self.parent.config = self.cfg
        self.destroy()
