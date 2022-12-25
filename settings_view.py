from tkinter import ttk
from tkinter import *

from game import Settings, DominoType, Player


def draw_settings_form(parent: Tk, init_cb):
    frame = ttk.Frame(parent)
    frame.grid()

    opponent_val = IntVar(value = Player.HUMAN.value)

    ttk.Radiobutton(parent, 
               text = "PvP",
               variable = opponent_val,
               padding = 20,
               value = Player.HUMAN.value).grid(row = 0, column = 0)
    ttk.Radiobutton(parent, 
                text = "PvAI",
                variable = opponent_val, 
                value = Player.AI.value).grid(row = 0, column = 1)


    first_player_val = IntVar(value = Player.HUMAN.value)

    ttk.Radiobutton(parent, 
               text = "Human first",
               variable = first_player_val,
               padding = 20,
               value = Player.HUMAN.value).grid(row = 1, column = 0)
    ttk.Radiobutton(parent, 
                text = "AI first",
                variable = first_player_val, 
                value = Player.AI.value).grid(row = 1, column = 1)


    ttk.Label(frame, text = 'Rows:', justify = LEFT).grid(row = 2, column = 0)
    rows_val = IntVar(value = 8)
    ttk.Spinbox(frame, from_ = 4, to = 16, width = 4,
                textvariable = rows_val).grid(row = 2, column = 1)

    ttk.Label(frame, text = 'Columns:', justify = LEFT).grid(row = 3, column = 0)
    cols_val = IntVar(value = 8)
    ttk.Spinbox(frame, from_ = 4, to = 16, width = 4,
                textvariable = cols_val).grid(row = 3, column = 1)

    ttk.Button(frame, text = 'Play', padding = 6, command = lambda: init_cb(Settings(
        m = rows_val.get(),
        n = cols_val.get(),
        starting_domino_type = DominoType.HORIZONTAL,
        opponent = Player(opponent_val.get()), 
        first_player = Player(first_player_val.get())))).grid(row = 4, column = 0, columnspan = 3)

    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)