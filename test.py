import tkinter as tk
import time
from tkinter import *
from PIL import Image, ImageTk

win = tk.Tk()
win.geometry('1600x900')  # set window size
win.resizable(False, False)  # fix window

canvas = Canvas(win, width=1600, height=900, bg="white")
canvas.pack(pady=0)

track_image = ImageTk.PhotoImage(Image.open('image/track.png'))
track_frame = canvas.create_image(100, 100, anchor=W, image=track_image)

# def car1():
car1_image = Image.open('image/tesla.png')
car1_resize = car1_image.resize((184, 428), Image.ANTIALIAS)
car1_drive = ImageTk.PhotoImage(car1_resize)
car1_frame = canvas.create_image(50, 50, anchor=NW, image=car1_drive)

car2_image = Image.open('image/car2.png')
car2_resize = car2_image.resize((428, 184), Image.ANTIALIAS)
car2_drive = ImageTk.PhotoImage(car2_resize)
car2_frame = canvas.create_image(50, 50, anchor=NW, image=car2_drive)

# for x in track_frame:
#    if elapsed_time == <3000:
#track_frame = 300


def __init__(self, master=None):
    self.master = ImageTk.PhotoImage(Image.open('image/tesla.png'))

    # to take care movement in x direction
    self.x = 0
    # to take care movement in y direction
    self.y = 0

    # canvas object to create shape
    self.canvas = Canvas(master)
    # creating rectangle
    self.rectangle = self.canvas.create_rectangle(
        5, 5, 25, 25, fill="black")
    self.canvas.pack()

    # calling class's movement method to
    # move the rectangle
    self.movement()


def movement(self):

    # This is where the move() method is called
    # This moves the rectangle to x, y coordinates
    self.canvas.move(self.rectangle, self.x, self.y)

    self.canvas.after(1000, self.movement)


def left(e):
    x = -20
    y = 0
    canvas.move(car1_frame, x, y)


def right(e):
    x = 20
    y = 0
    canvas.move(car1_frame, x, y)


def up(e):
    x = 0
    y = -20
    canvas.move(car1_frame, x, y)


def down(e):
    x = 0
    y = 20
    canvas.move(car1_frame, x, y)


def left2(e):
    x = -20
    y = 0
    canvas.move(car2_frame, x, y)


def righ2t(e):
    x = 20
    y = 0
    canvas.move(car2_frame, x, y)


def up2(e):
    x = 0
    y = -20
    canvas.move(car2_frame, x, y)


def down2(e):
    x = 0
    y = 20
    canvas.move(car2_frame, x, y)


def track_scroll(e):
    x = 0
    y = -50
    canvas.move(track_frame, x, y)


if __name__ == "__main__":
    # Bind the move function
    #win.bind("<Left>", left)
    #win.bind("<Right>", right)
    win.bind("<Up>", up)
    win.bind("<Down>", down)
    win.bind("<w>", up2)
    win.bind("<s>", down2)

# while True:
#    canvas.move()

win.mainloop()
