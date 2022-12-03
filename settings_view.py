from tkinter import ttk
from tkinter import *

from game import Settings, GameMode, DominoType


def draw_settings_form(parent: Tk, init_cb):
    frame = ttk.Frame(parent)
    frame.grid()

    game_mode_val = IntVar(value = GameMode.PVP.value)

    ttk.Radiobutton(parent, 
               text = "PvP",
               variable = game_mode_val,
               padding = 20,
               value = GameMode.PVP.value).grid(row = 0, column = 0)
    ttk.Radiobutton(parent, 
                text = "PvAI",
                variable = game_mode_val, 
                value = GameMode.PVAI.value).grid(row = 0, column = 1)

    ttk.Label(frame, text = 'Rows:', justify = LEFT).grid(row = 1, column = 0)
    rows_val = IntVar(value = 8)
    ttk.Spinbox(frame, from_ = 4, to = 16, width = 4,
                textvariable = rows_val).grid(row = 1, column = 1)

    ttk.Label(frame, text = 'Columns:', justify = LEFT).grid(row = 2, column = 0)
    cols_val = IntVar(value = 8)
    ttk.Spinbox(frame, from_ = 4, to = 16, width = 4,
                textvariable = cols_val).grid(row = 2, column = 1)

    ttk.Button(frame, text = 'Play', padding = 6, command = lambda: init_cb(Settings(
        m = rows_val.get(),
        n = cols_val.get(),
        starting_domino_type = DominoType.VERTICAL,
        game_mode = GameMode(game_mode_val.get())))).grid(row = 3, column = 0, columnspan = 3)

    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)