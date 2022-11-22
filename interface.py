from tkinter import *
from tkinter import ttk

from game import *

def initSettingWindow():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    label = ttk.Label(
        text="Hello, Tkinter",
        foreground="white",
        background="black" 
    ).grid(column=0, row=1)

    m = 5
    n = 8

    root.mainloop()
    return { 'm': m, 'n': n }

def initGameWindow(settings: dict):
    g = Game()

    g.init(settings['m'], settings['n'])
    print(g.board)

    root = Tk()

    root.mainloop()

settings = initSettingWindow()
initGameWindow(settings)