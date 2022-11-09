import tkinter as tk
import time
import tk_sleep
from tkinter import *
from PIL import Image, ImageTk
from tk_sleep import tk_sleep


win = tk.Tk()
win.geometry('1600x900')  # set window size
win.resizable(False, False)  # fix window
img = Image.open("image/race_track.png")
image1 = ImageTk.PhotoImage(img)
reference_to_image = Canvas(win)
reference_to_image.image = image1

canvas = Canvas(win, width=1600, height=900)
canvas.pack(pady=0)

track_image = Image.open('image/full_track.png')
track_image1 = ImageTk.PhotoImage(track_image)
track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image1)

start_time = time.time()
end_time = (start_time + 25)

#track_image = ImageTk.PhotoImage(Image.open('image/race_track.png'))
#track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image)


def car():
    car1_image = Image.open('image/tesla.png')
    car1_resize = car1_image.resize((214, 92), Image.ANTIALIAS)
    car1_drive = ImageTk.PhotoImage(car1_resize)
    car1_frame = canvas.create_image(50, 200, anchor=NW, image=car1_drive)


car1_image = Image.open('image/tesla.png')
car1_resize = car1_image.resize((214, 92), Image.ANTIALIAS)
car1_drive = ImageTk.PhotoImage(car1_resize)
car1_frame = canvas.create_image(50, 200, anchor=NW, image=car1_drive)

car2_image = Image.open('image/car2.png')
car2_resize = car2_image.resize((214, 92), Image.ANTIALIAS)
car2_drive = ImageTk.PhotoImage(car2_resize)
car2_frame = canvas.create_image(50, 600, anchor=NW, image=car2_drive)

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


if __name__ == "__main__":
    # Bind the move function
    #win.bind("<Left>", left)
    #win.bind("<Right>", right)
    win.bind("<Up>", up)
    win.bind("<Down>", down)
    win.bind("<w>", up2)
    win.bind("<s>", down2)


def track_scroll():
    tk_sleep(win, 1/60)
    track_move = canvas.move(track_frame, -15, 0)


def game_time():
    if start_time == end_time:
        print('time up')
    else:
        time.sleep(25)
        if start_time <= end_time:
            print('25 seconds have passed')
        else:
            print('no time')


def game_start():
    while True:
        track_scroll()
        if start_time > end_time:
            break


game_start()
win.mainloop()
