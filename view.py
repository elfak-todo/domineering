from tkinter import Canvas
from game import Settings

square_size = 80

square_dark_color = '#999999'
square_light_color = '#fefefe'

domino_dark_color = '#403c33'
domino_light_color = '#d4643c'

def draw_table(parent, settings: Settings):
    row_count = settings.m
    column_count = settings.n

    dark = False

    canvas = Canvas(parent, width=square_size * column_count, height=square_size * row_count)

    for y in range(row_count):
        for x in range(column_count):
            fill = square_dark_color if dark else square_light_color
            canvas.create_rectangle(x * square_size, y * square_size, (x + 1) * square_size, (y + 1) * square_size, fill=fill, outline=fill)
            dark = not dark
        dark = not dark

    canvas.pack(padx=40, pady=40)

    return canvas

def draw_domino(canvas: Canvas, cursor_x, cursor_y, domino_type, hover = False):
    cnt_x = cnt_y = -1

    while cursor_x > 0:
        cursor_x -= square_size
        cnt_x += 1
    while cursor_y > 0:
        cursor_y -= square_size
        cnt_y += 1

    offset = square_size / 10

    x0 = cnt_x * square_size + offset
    y0 = cnt_y * square_size + offset

    x1 = x0 + square_size - 2 * offset
    y1 = y0 + square_size - 2 * offset

    if (domino_type):
        x1 += square_size
        fill = domino_dark_color if not hover else '#c5c4c1'
    else:
        y0 -= square_size
        fill = domino_light_color if not hover else '#f2d0c4'

    canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=domino_dark_color, tags='hover' if hover else None)


def draw_hover_domino(canvas, cursor_x, cursor_y, domino_type):
    canvas.delete('hover')
    draw_domino(canvas, cursor_x, cursor_y, domino_type, True)
