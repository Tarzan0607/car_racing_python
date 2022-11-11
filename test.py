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

# car_track.tkraise()


def boost1():
    print('boost1')


def boost_scroll():
    print()


obstacle_image = Image.open('image/obstacle.png')
obstacle_image1 = ImageTk.PhotoImage(obstacle_image)
obstacle_item = canvas.create_image(
    1600, random.randint(50, 850), image=obstacle_image1)

boost_image = Image.open('image/boost.png')
boost_image1 = ImageTk.PhotoImage(boost_image)
boost_item = canvas.create_image(
    1600, random.randint(50, 850), image=boost_image1)


def boosts():
    boost_item = canvas.create_image(
        1600, random.randint(50, 850), image=boost_image1)


canvas.after(1000, boosts)

boost2 = time.time() + 3
boost3 = time.time() + 5
boost4 = time.time() + 7
boost5 = time.time() + 9
boost6 = time.time() + 11
boost7 = time.time() + 13
boost8 = time.time() + 15
boost9 = time.time() + 17
boost10 = time.time() + 19

obstacle1 = time.time() + 2
obstacle2 = time.time() + 4
obstacle3 = time.time() + 6
obstacle4 = time.time() + 8
obstacle5 = time.time() + 10
obstacle6 = time.time() + 12
obstacle7 = time.time() + 14
obstacle8 = time.time() + 16
obstacle9 = time.time() + 18

end_time = time.time() + 20


def win_line():
    print


def win_line_scroll():
    canvas.after(20000, print('game done'))
    tk_sleep(win, 1/60)
    track_move = canvas.move(track_frame, -15, 0)


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


'''
def track():
    for count in range(10):
        canvas = Canvas(win)
        canvas.pack(side=TOP)
    for counter in range(10):
        label1 = Label(canvas, image=image1,
                           borderwidth=0, highlightthickness=0)
        label1.pack(side=LEFT)
    return canvas
'''


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


def movement(self):

    # This is where the move() method is called
    # This moves the rectangle to x, y coordinates
    self.canvas.move(self.rectangle, self.x, self.y)

    self.canvas.after(1000, self.movement)


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
    obstacle_move = canvas.move(obstacle_item, -10, 0)
    boost_move = canvas.move(boost_item, -10, 0)


def game_time():
    if start_time == end_time:
        print('time up')
    else:
        time.sleep(25)
        if start_time <= end_time:
            print('25 seconds have passed')
        else:
            print('no time')


win.after(1000, boost1)

win.after(20000, win_line)


def game_loop():
    while True:
        track_scroll()

        if time.time() > end_time:
            break


game_loop()
win.mainloop()
