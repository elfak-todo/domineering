from tkinter import *
from tkinter import ttk
from tkinter import Canvas

from game import Settings
from game import Game


square_size = 80

square_dark_color = '#999999'
square_light_color = '#fefefe'

domino_dark_color = '#403c33'
domino_light_color = '#d4643c'

def draw_table(parent, settings: Settings):
    row_count = settings.m
    column_count = settings.n
    dark = False
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    canvas_main = Canvas(parent, width=square_size * column_count +
                         square_size, height=square_size * row_count + square_size)
    canvas = Canvas(canvas_main, width=square_size *
                    column_count, height=square_size * row_count)

    for y in range(row_count):
        for x in range(column_count):
            fill = square_dark_color if dark else square_light_color
            canvas.create_rectangle(x * square_size, y * square_size, (x + 1)
                                    * square_size, (y + 1) * square_size, fill=fill, outline=fill)
            dark = not dark
        dark = not dark

    for y in range(row_count):
        canvas_main.create_text(2, y * square_size + square_size / 2 + 10,
                                text=y + 1, anchor='nw', font=('TkMenuFont', '12'), fill='black')
    for x in range(column_count):
        canvas_main.create_text(x * square_size + square_size / 2 + 10, row_count * square_size +
                                22, text=letters[x], anchor='nw', font=('TkMenuFont', '12'), fill='black')

    canvas.pack(padx=20, pady=20)
    canvas_main.pack(padx=20, pady=20)

    return canvas

def draw_form(parent: Tk, init_cb):
    frame = ttk.Frame(parent)

    ttk.Label(frame, text='Rows:').grid(row=0, column=0)
    rows_val = IntVar(value=8)
    ttk.Spinbox(frame, from_=4, to=16, width=4,
                textvariable=rows_val).grid(row=0, column=1)

    ttk.Label(frame, text='Columns:').grid(row=1, column=0)
    cols_val = IntVar(value=8)
    ttk.Spinbox(frame, from_=4, to=16, width=4,
                textvariable=cols_val).grid(row=1, column=1)

    pvp = BooleanVar(value=False)
    ttk.Checkbutton(frame, text='Versus AI', variable=pvp).grid(
        row=2, column=0, columnspan=2)

    ttk.Button(frame, text='Play', padding=5, command=lambda: init_cb(Settings(
        rows_val.get(), cols_val.get(), 0, not pvp.get()))).grid(row=3, column=0, columnspan=2)

    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def draw_domino(canvas: Canvas, cursor_x, cursor_y, domino_type, hover=False):

    cnt_x = int(cursor_x / square_size)
    cnt_y = int(cursor_y / square_size)

    offset = square_size / 10

    x0 = cnt_x * square_size + offset
    y0 = cnt_y * square_size + offset

    x1 = x0 + square_size - 2 * offset
    y1 = y0 + square_size - 2 * offset

    if (domino_type):
        x1 += square_size
        fill = domino_dark_color
    else:
        y0 -= square_size
        fill = domino_light_color
        
    #Sprecava iscrtavanje van okvira table
    if x0 > 0 and y0 > 0 and x1 < canvas.winfo_width():
        canvas.create_rectangle(
            x0, y0, x1, y1, fill=fill, outline=domino_dark_color, tags='hover-domino' if hover else None)


def draw_hover_domino(canvas, cursor_x, cursor_y, domino_type):
    canvas.delete('hover-domino')
    draw_domino(canvas, cursor_x, cursor_y, domino_type, True)
