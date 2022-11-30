from tkinter import *

from game import *
from view import *


def init_settings_window():
    root = Tk()
    root.title('Settings')
    root.resizable(False, False)

    win_w = 300
    win_h = 150

    x = root.winfo_screenwidth() / 2 - win_w / 2
    y = root.winfo_screenheight() / 2 - win_h / 2

    root.geometry('{}x{}+{}+{}'.format(win_w, win_h, int(x), int(y)))

    draw_form(root, init_game_window)

    root.mainloop()


def init_game_window(settings: Settings):
    game = Game()
    game.init(settings.m, settings.n, settings.domino_type)

    root = Tk()
    root.title('Domineering')
    root.resizable(False, False)

    canvas = draw_table(root, settings)

    canvas.bind('<Button 1>', lambda event: draw_domino(
        canvas, event.x, event.y, game.swap()))
    canvas.bind('<Motion>', lambda event: draw_hover_domino(
        canvas, event.x, event.y, not game.d_type))

    root.mainloop()


init_settings_window()

