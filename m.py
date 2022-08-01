import tkinter as tk
from tkinter import *
from Posicionamento import *


class Facer(tk.Tk):
    def Proximo(self):
        Facer.forget()
        Movie.pack()

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Tibira")
        self.minsize(width=1023, height=755)
        self.maxsize(width=1023, height=755)

        lubs = tk.Frame(self)
        interface = tk.Label(self, background='Black')
        but = tk.Button(self, bg='Blue', command=Proximo())
        lubs.pack()
        interface.pack()
        but.pack()








class Movie(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global interfacer
        interfacer = PhotoImage(file=r'2.png')
        labelInter= tk.Label(self, image=interfacer)
        labelInter.after(3000, labelInter.forget)
        labelInter.pack()





if __name__=="__main__":
    root = Facer()
    root.mainloop()
