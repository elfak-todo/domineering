from tkinter import ttk
from tkinter import *

from game import Settings, DominoType, Player


def draw_settings_form(parent: Tk, init_cb):
    frame = ttk.Frame(parent)
    frame.pack()

    first_player_frame = ttk.LabelFrame(frame, text="First player", padding=5)
    first_player_val = IntVar(value=Player.HUMAN.value)

    radio1 = ttk.Radiobutton(first_player_frame, 
                text="Human first",
                variable=first_player_val,
                value=Player.HUMAN.value,
                state=DISABLED)
    radio2 = ttk.Radiobutton(first_player_frame, 
                text="AI first",
                variable=first_player_val, 
                value=Player.AI.value,
                state=DISABLED)

    radio1.grid(row=0, column=0)
    radio2.grid(row=0, column=1)

    first_player_frame.grid(row=1, column=0)

    opponent_frame = ttk.LabelFrame(frame, text="Game mode", padding=5)
    opponent_val = IntVar(value=Player.HUMAN.value)

    ttk.Radiobutton(opponent_frame, 
                text="PvP",
                variable=opponent_val,
                value=Player.HUMAN.value,
                command=lambda: radio1.configure(state=DISABLED) or radio2.configure(state=DISABLED)).grid(row=0, column=0)
    ttk.Radiobutton(opponent_frame, 
                text="PvAI",
                variable=opponent_val, 
                value=Player.AI.value,
                command=lambda: radio1.configure(state=NORMAL) or radio2.configure(state=NORMAL)).grid(row=0, column=1)

    opponent_frame.grid(row=0, column=0)


    board_frame = ttk.LabelFrame(frame, text="Board size", padding=5)

    ttk.Label(board_frame, text='Rows:', justify=RIGHT).grid(row=0, column=0)

    rows_val = IntVar(value=8)
    ttk.Spinbox(board_frame, from_=4, to=16, width=4,
                textvariable=rows_val).grid(row=0, column=1)

    ttk.Label(board_frame, text='Columns:', justify=RIGHT).grid(row=1, column=0)
    cols_val = IntVar(value=8)
    ttk.Spinbox(board_frame, from_=4, to=16, width=4,
                textvariable=cols_val).grid(row=1, column=1)

    board_frame.grid(row=3, column=0)

    ttk.Button(frame, text='Play', padding=8, command=lambda: init_cb(Settings(
        m=rows_val.get(),
        n=cols_val.get(),
        starting_domino_type=DominoType.HORIZONTAL,
        opponent=Player(opponent_val.get()), 
        first_player=Player(first_player_val.get())))).grid(row=4, column=0)

    frame.place(relx=0.5, rely=0.5, anchor=CENTER)