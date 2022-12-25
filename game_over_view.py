from tkinter import Tk, ttk, CENTER


def draw_game_over(message: str):
    root = Tk()
    root.title('Game over!')
    root.resizable(False, False)

    win_w = 250
    win_h = 100

    x = root.winfo_screenwidth() / 2 - win_w / 2
    y = root.winfo_screenheight() / 2 - win_h / 2

    root.geometry('{}x{}+{}+{}'.format(win_w, win_h, int(x), int(y)))

    frame = ttk.Frame(root)
    frame.grid()

    ttk.Label(frame, text=message, justify=CENTER, padding=6).grid(row=0, column=0)

    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()