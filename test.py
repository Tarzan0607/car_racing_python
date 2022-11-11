import tkinter as tk
import time
import datetime
import tk_sleep
import random
from tkinter import *
from PIL import Image, ImageTk
from tk_sleep import tk_sleep
from datetime import datetime

win = tk.Tk()
win.geometry('1600x900')  # set window size
win.resizable(False, False)  # fix window
img = Image.open("image/race_track.png")
image1 = ImageTk.PhotoImage(img)
reference_to_image = Canvas(win)
reference_to_image.image = image1

canvas = Canvas(win, width=1600, height=900)
canvas.pack()


track_frame1 = Frame(canvas, height=900, width=1600)
track_image = Image.open('image/full_track.png')
track_image1 = ImageTk.PhotoImage(track_image)
track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image1)

car_track = Frame(canvas, height=700, width=1600, bg='white')


car_track1 = Image.open('image/tesla.png')
car_track2 = ImageTk.PhotoImage(car_track1)
car_track_frame = canvas.create_image(0, 100-800, image=car_track2)

car1_image = Image.open('image/tesla.png')
car1_resize = car1_image.resize((214, 92), Image.ANTIALIAS)
car1_drive = ImageTk.PhotoImage(car1_resize)
car1_frame = canvas.create_image(150, 200, anchor=NW, image=car1_drive)

car2_image = Image.open('image/car2.png')
car2_resize = car2_image.resize((214, 92), Image.ANTIALIAS)
car2_drive = ImageTk.PhotoImage(car2_resize)
car2_frame = canvas.create_image(150, 600, anchor=NW, image=car2_drive)

obstacle_image = Image.open('image/obstacle.png')
obstacle_image1 = ImageTk.PhotoImage(obstacle_image)

boost_image = Image.open('image/boost.png')
boost_image1 = ImageTk.PhotoImage(boost_image)

win_line = Image.open('image/finishline.png')
win_line1 = ImageTk.PhotoImage(win_line)
#win_item = canvas.create_image(1600, 100, anchor=NE, image=win_line1)


def obstacle_item():
    global obstacle_item
    obstacle_item = canvas.create_image(
        1600, random.randint(150, 750), image=obstacle_image1)


def boost_item():
    global boost_item
    boost_item = canvas.create_image(
        1600, random.randint(150, 750), image=boost_image1)


def win_line2():
    global win_line2
    win_line2 = canvas.create_image(1600, 100, anchor=NE, image=win_line1)


win.after(1000, boost_item)
win.after(3000, boost_item)
win.after(5000, boost_item)
win.after(7000, boost_item)
win.after(9000, boost_item)
win.after(11000, boost_item)
win.after(13000, boost_item)
win.after(15000, boost_item)
win.after(17000, boost_item)
win.after(19000, boost_item)

win.after(2000, obstacle_item)
win.after(4000, obstacle_item)
win.after(6000, obstacle_item)
win.after(8000, obstacle_item)
win.after(10000, obstacle_item)
win.after(12000, obstacle_item)
win.after(14000, obstacle_item)
win.after(16000, obstacle_item)
win.after(18000, obstacle_item)

win.after(20000, win_line2)

end_time = time.time() + 22


def channel_user(user, message):
    # who is the server (= the creator of the channel)
    if 'created the channel' in message:
        name = message.split("'")[1]
        game_state['is_server'] = name == game_state['me']
    # who is the opponent (= the one that joined that is not me)
    if 'joined channel' in message:
        name = message.split(' ')[1]
        if name != game_state['me']:
            game_state['opponent'] = name

#track_image = ImageTk.PhotoImage(Image.open('image/race_track.png'))
#track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image)


def __init__(self, master=None):
    self.master = ImageTk.PhotoImage(Image.open())

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


def up(e):
    x = 0
    y = -20
    canvas.move(car1_frame, x, y)


def down(e):
    x = 0
    y = 20
    canvas.move(car1_frame, x, y)


def up2(e):
    x = 0
    y = -20
    canvas.move(car2_frame, x, y)


def down2(e):
    x = 0
    y = 20
    canvas.move(car2_frame, x, y)


if __name__ == "__main__":
    # Bind the move function

    win.bind("<Up>", up)
    win.bind("<Down>", down)
    win.bind("<w>", up2)
    win.bind("<s>", down2)


def track_scroll():
    tk_sleep(win, 1/60)
    track_move = canvas.move(track_frame, -15, 0)
    obstacle_move = canvas.move(obstacle_item, -15, 0)
    boost_move = canvas.move(boost_item, -15, 0)
    win_line_move = canvas.move(win_line2, -15, 0)


def game_loop():
    while True:
        track_scroll()
        if time.time() > end_time:
            break


game_loop()
win.mainloop()
