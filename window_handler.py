def load_window(tk, title, size_y, size_x):
    gamewindow = tk.Tk()

    gamewindow.title(title)

    screen_width = gamewindow.winfo_screenwidth()
    screen_height = gamewindow.winfo_screenheight()

    window_width = round(size_x)
    window_height = round(size_y)

    center_x = round(screen_width / 2 - window_width / 2)
    center_y = round(screen_height / 2 - window_height / 2)

    gamewindow.geometry(
        f'{window_width}x{window_height}+{center_x}+{center_y}')
    return gamewindow


def start_window_loop(gamewindow):
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    finally:
        gamewindow.mainloop()
