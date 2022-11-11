import tkinter as tk
from random import randint
from tkinter import simpledialog
from window_handler import load_window, start_window_loop

game_area_width = 1600
game_area_height = 900

window = create_window(tk, 'Python 2player racing game')

# def start()
game_name = simpledialog.askstring('Player name', 'What is your playerID?',
                                   parent=gamewindow)
game_channel = simpledialog.askstring('Game channel', 'Enter game room name',
                                      parent=gamewindow)
start_window_loop(gamewindow)
