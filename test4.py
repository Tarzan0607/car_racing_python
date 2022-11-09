import time
import tkinter as tk
from tkinter.ttk import Label
from time import sleep
from tkinter import *
from PIL import Image, ImageTk
from tk_sleep import tk_sleep

start_time = time.time()
end_time = (start_time + 25)


def game_time():
    if start_time == end_time:
        print('time up')
    else:
        time.sleep(3)
        if start_time <= end_time:
            print('25 seconds have passed')
        else:
            print('no time')


root = tk.Tk()
root.geometry('1600x900')

canvas = Canvas(root, width=1600, height=900)
canvas.pack(pady=0)

track_image = Image.open('image/full_track.png')
track_image1 = ImageTk.PhotoImage(track_image)
track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image1)


def left_scroll(e):
    x = -3000
    y = 0
    canvas.move(track_frame, x, y)


def track_scroll():
    tk_sleep(root, 1/60)
    track_move = canvas.move(track_frame, -15, 0)


while True:
    track_scroll()

#root.after(500, left_scroll)

#root.bind("<a>", left_scroll)

root.mainloop()
