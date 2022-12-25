from tkinter import *
from tkinter import Canvas

from game import Settings, DominoType, Status
from game_over_view import draw_game_over

SQUARE_SIZE = 80

SQUARE_DARK_COLOR = '#999999'
SQUARE_LIGHT_COLOR = '#fefefe'

DOMINO_DARK_COLOR = '#403c33'
DOMINO_LIGHT_COLOR = '#d4643c'

def draw_table(parent, settings: Settings):
    row_count = settings.m
    column_count = settings.n
    dark = False

    canvas_main = Canvas(parent, width=SQUARE_SIZE * column_count +
                         SQUARE_SIZE, height=SQUARE_SIZE * row_count + SQUARE_SIZE)
    canvas = Canvas(canvas_main, width = SQUARE_SIZE *
                    column_count, height = SQUARE_SIZE * row_count)

    for y in range(row_count):
        for x in range(column_count):
            fill = SQUARE_DARK_COLOR if dark else SQUARE_LIGHT_COLOR
            canvas.create_rectangle(x * SQUARE_SIZE, y * SQUARE_SIZE, (x + 1)
                                    * SQUARE_SIZE, (y + 1) * SQUARE_SIZE, fill = fill, outline = fill)
            dark = not dark
        if column_count % 2 == 0:   
            dark = not dark

    for y in range(row_count):
        canvas_main.create_text(2, y * SQUARE_SIZE + SQUARE_SIZE / 2 + 10,
                                text = y + 1, anchor = NW, font = ('TkMenuFont', '12'), fill = 'black')
    for x in range(column_count):
        canvas_main.create_text(x * SQUARE_SIZE + SQUARE_SIZE / 2 + 10, row_count * SQUARE_SIZE +
                                22, text = chr(ord('A') + x), anchor = NW, font = ('TkMenuFont', '12'), fill = 'black')

    canvas.pack(padx = 20, pady = 20)
    canvas_main.pack(padx = 20, pady = 20)

    return canvas

def draw_domino(canvas: Canvas, cursor_x, cursor_y, domino_type, game, hover = False):
    if game.status is not Status.PLAYING:
        return
        
    cnt_x = int(cursor_x / SQUARE_SIZE)
    cnt_y = int(cursor_y / SQUARE_SIZE)

    if not game.is_move_valid(game.board, cnt_x, cnt_y, domino_type):
        return

    offset = SQUARE_SIZE / 10

    x0 = cnt_x * SQUARE_SIZE + offset
    y0 = cnt_y * SQUARE_SIZE + offset

    x1 = x0 + SQUARE_SIZE - 2 * offset
    y1 = y0 + SQUARE_SIZE - 2 * offset

    if (domino_type is DominoType.HORIZONTAL):
        x1 += SQUARE_SIZE
        fill = DOMINO_DARK_COLOR
    else:
        y0 -= SQUARE_SIZE
        fill = DOMINO_LIGHT_COLOR

    if not hover:
        game.make_a_move(cnt_x, cnt_y, domino_type)
        print(game.minimax(game.board, 2, domino_type))

    canvas.create_rectangle(
        x0, y0, x1, y1, fill = fill, outline = DOMINO_DARK_COLOR, tags = 'hover-domino' if hover else None)

    if game.status is Status.HORIZONTAL_WON:
        draw_game_over('Horizontal player won!')
    elif game.status is Status.VERTICAL_WON:
        draw_game_over('Vertical player won!')

def draw_hover_domino(canvas, cursor_x, cursor_y, domino_type, game):
    canvas.delete('hover-domino')
    draw_domino(canvas, cursor_x, cursor_y, domino_type, game, True)
