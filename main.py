from tkinter import *

from game import *
from game_view import *
from settings_view import *


def init_settings_window():
    root = Tk()
    root.title('Settings')
    root.resizable(False, False)

    win_w = 230
    win_h = 230

    x = root.winfo_screenwidth() / 2 - win_w / 2
    y = root.winfo_screenheight() / 2 - win_h / 2

    root.geometry('{}x{}+{}+{}'.format(win_w, win_h, int(x), int(y)))

    draw_settings_form(root, init_game_window)

    root.mainloop()


def init_game_window(settings: Settings):
    game = Game(settings.m, settings.n, settings.starting_domino_type, settings.opponent, settings.first_player)
    
    root = Tk()
    root.title('Domineering')
    root.resizable(False, False)

    canvas = draw_table(root, settings)

    canvas.bind('<Button 1>', lambda event: on_click(
        canvas, event.x, event.y, swap(game.d_type), game))
    canvas.bind('<Motion>', lambda event: on_hover(
        canvas, event.x, event.y, swap(game.d_type), game))

    if settings.opponent == Player.AI and settings.first_player == Player.AI:
        play_ai_move(canvas, settings.starting_domino_type, game)

    root.mainloop()

init_settings_window()

