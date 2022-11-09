import time
import tkinter as tk
from tkinter.ttk import Label
from time import sleep
from tkinter import *
from PIL import Image, ImageTk
import random

# define window massage
root = tk()
root.geometry("#the fdisplay size")
root.title("Our game")

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
track_image = ImageTk.PhotoImage(Image.open('image/full_track.png'))
track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image)


def left_scroll(e):
    x = -50
    y = 0
    canvas.move(track_frame, x, y)

# img = Image.open('image/race_track.png')

# placing the collition image on the track !!


# keep collision set random
def keep_collision_random():
    collision_x = random.randint()  # need to set value
    collision_y = random.randint()  # need to set value
    # collision need to define  or create first
    track_frame.coords(collision, collision_x, collision_y)


root.bind("<a>", left_scroll)

# ---------  ****** . ---------

# move the car right


def moveright(event):
    track_frame.move(car, 10, 0)
    car_edge_reached()
    collision_detection()
# move the car left


def moveleft(event):
    for i in range(10):
        track_frame.move(car, -1, 0)
        car_edge_reached()
        collision_detection()

# car reached the edge or not


def car_edge_reached():
    car_boundary = track_frame.track(car)
    car_left = car_boundary[0]
    car_right = car_boundary[0]

    if car_left < 0:
        track_frame.move(car, 10, 0)
    else car_right < 0:
        track_frame.move(car, 0, 10)

 # ditect the collition


def collision_detection():
    car = track_frame.track(car)


#  starting the random movement function
keep_collision_random()


# making the car move
track_frame.blind_all("<Right>", moveright)
track_frame.blind_all("<a>", moveleft)

root.mainloop()
