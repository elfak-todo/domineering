from tkinter import *
from tkinter import ttk

from game import *
from view import *


def init_setting_window():
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
    return {'m': m, 'n': n}


def init_game_window(settings: dict):
    g = Game()
    g.init(settings['m'], settings['n'], settings['domino_type'])

    root = Tk()
    root.resizable(False, False)

    canvas = draw_table(root, settings)
    canvas.bind('<Button 1>', lambda event: draw_domino(canvas, event.x, event.y, g.swap()))

    root.mainloop()


# settings = init_setting_window()
settings = {'m': 8, 'n': 8, 'domino_type': 0}
init_game_window(settings)
