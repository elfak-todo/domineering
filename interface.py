from tkinter import *
from tkinter import ttk

from game import *
from view import *


def init_settings_window():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    settings = Settings()
    settings.m = 8
    settings.n = 8

    root.mainloop()
    return settings


def init_game_window(settings: Settings):
    game = Game()
    game.init(settings.m, settings.n, settings.domino_type)

    root = Tk()
    root.title('Domineering')
    root.resizable(False, False)
    
    canvas = draw_table(root, settings)
    
    canvas.bind('<Button 1>', lambda event: draw_domino(canvas, event.x, event.y, game.swap()))
    canvas.bind('<Motion>', lambda event: draw_hover_domino(canvas, event.x, event.y, not game.d_type))

    root.mainloop()


settings = init_settings_window()
init_game_window(settings)
