#import some files right there:
#_______________________________________________________________________________________________________________________
import Posicionamento
from tkinter import *
import tkinter as tk
#from tkcalendar import *
#_______________________________________________________________________________________________________________________
from Posicionamento import *
#_______________________________________________________________________________________________________________________
def menu():
    Interface.forget()
    Menu.pack()


class Face(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Tibira")

        # creating a frame and assigning it to container
        f0 = tk.Frame(self, bg='Black', border=0)
        # specifying the region where the frame is packed in root
        f0.pack(expand=False)

        self.minsize(width=1023, height=755)
        self.maxsize(width=1023, height=755)

        # configuring the location of the container using grid
        f0.grid_rowconfigure(0, weight=1)
        f0.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (Interface, Menu, CompletionScreen):
            frame = F(f0, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(Interface)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class Interface(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global interfacer
        interfacer = PhotoImage(file=r'2.png')
        labelInter= tk.Label(self, image=interfacer)
        labelInter.after(3000, labelInter.forget)
        labelInter.pack()



        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        lub= PhotoImage(file=r'3.png')
        sds=tk.Frame(self)
        lus=tk.Label(sds, image=lub)
        switch_window_button = tk.Button(
            sds,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(Menu),
        )
        lus.pack()
        sds.pack()
        switch_window_button.grid(row=3,column=4)


class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global men
        men = PhotoImage(file=r'3.png')
        menu = tk.Label(self, image=men)
        menu.pack()



class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack()
        switch_window_button = tk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(Interface)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)
if __name__ == "__main__":
    root = Face()
    # verificar os pixels
    root.bind('<Button-1>', Poc.inicio_place)
    root.bind('<ButtonRelease-1>', lambda arg: Poc.fim_place(arg, root))
    root.bind('<Button-2>', lambda arg: Poc.para_geometry(root))
    root.mainloop()





    





















