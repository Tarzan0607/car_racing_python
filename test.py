import tkinter as tk
import time
import datetime
import tk_sleep
import random
import bbox
from network import connect, send
from tkinter import *
from PIL import Image, ImageTk
from tk_sleep import tk_sleep
from datetime import datetime
from tkinter import simpledialog
from bbox import bbox2d

win = tk.Tk()
win.geometry('1600x900')  # set window size
win.resizable(False, False)  # fix window
img = Image.open("image/race_track.png")
image1 = ImageTk.PhotoImage(img)
reference_to_image = Canvas(win)
reference_to_image.image = image1
#message = Label(win, style='Message.TLabel')
info_1 = Label(win)
info_2 = Label(win)


canvas = Canvas(win, width=1600, height=900)
canvas.pack()


track_frame1 = Frame(canvas, width=1600, height=900, )
track_image = Image.open('image/full_track.png')
track_image1 = ImageTk.PhotoImage(track_image)
track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image1)


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
# win_item = canvas.create_image(1600, 100, anchor=NE, image=win_line1)


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


canvas.after(1000, boost_item)
canvas.after(3000, boost_item)
canvas.after(5000, boost_item)
canvas.after(7000, boost_item)
canvas.after(9000, boost_item)
canvas.after(11000, boost_item)
canvas.after(13000, boost_item)
canvas.after(15000, boost_item)
canvas.after(17000, boost_item)
canvas.after(19000, boost_item)

canvas.after(2000, obstacle_item)
canvas.after(4000, obstacle_item)
canvas.after(6000, obstacle_item)
canvas.after(8000, obstacle_item)
canvas.after(10000, obstacle_item)
canvas.after(12000, obstacle_item)
canvas.after(14000, obstacle_item)
canvas.after(16000, obstacle_item)
canvas.after(18000, obstacle_item)

canvas.after(20000, win_line2)

end_time = time.time() + 22


def car1_track_boundary(self):
    car1_edge = canvas.bbox(car1_frame)
    car1_left = car1_edge[0]
    car1_top = car1_edge[1]
    car1_right = car1_edge[2]
    car1_bottom = car1_edge[3]
    if car1_top < 720:
        canvas.move(car1_frame, 0, 15)
    if car1_bottom > 180:
        canvas.move(car1_frame, 0, -15)


def car2_track_boundary(self):
    car2_edge = canvas.bbox(car2_frame)
    car2_left = car2_edge[0]
    car2_top = car2_edge[1]
    car2_right = car2_edge[2]
    car2_bottom = car2_edge[3]
    if car2_top < 720:
        canvas.move(car2_frame, 0, 15)
    if car2_bottom > 180:
        canvas.move(car2_frame, 0, -15)


def boost_boundary():
    car1_edge = canvas.bbox(car1_frame)
    car2_edge = canvas.bbox(car2_frame)
    boost_edge = canvas.bbox(boost_item1)
    if boost_edge[0] < car1_edge[2] < boost_edge[2] and boost_edge[1] < car1_edge[1] < boost_edge[3]:
        canvas.move(car1_frame, 100, 0)
        canvas.delete('boost')
        print('collision')


def obstacle_boundary():
    car1_edge = canvas.bbox(car1_frame)
    car2_edge = canvas.bbox(car2_frame)
    obstacle_edge = canvas.bbox(obstacle_item1)
    if obstacle_edge[0] < car1_edge[2] < obstacle_edge[2] and obstacle_edge[1] < car1_edge[1] < obstacle_edge[3]:
        canvas.move(car1_frame, 100, 0)
        canvas.delete('boost')
        print('collision')


# some initial variables including a game state
# (tidy to keep everything in a dictionary
game_state = {
    'me': None,
    'opponent': None,
    'is_server': None,
    'shared': {
        'car1_image': '',
        'car2_image': '',
        'track_frame': '',
        'obstacle_item': '',
        'score_1': '',
        'score_2': '',
        'boost_image': '',
        'boost_image1': '',
        'lives_1': '',
        'lives_2': '',


        'game_over_message': ''
    }
}

# Draw the elements (car, obstracle , boost) on the screen


def redraw_screen():
    car1_image, car2_image, boost_image, boost_image1,\
        player_1, player_2, lives_1, lives_2,\
        score_1, score_2, game_over_message =\
        game_state['shared'].values()
    obstacle_item.place(x=boost_image, y=car1_image)
    obstacle_item.place(x=boost_image1, y=car2_image)

    boost_image.place(x=0, y=car1_image)
    boost_image1.place(x=980, y=car2_image)
    info_1.config(text=(
        f'\nPlayer: {player_1}\n' +
        f'Score: {score_1}\n' +
        f'Lives: {lives_1}'
    ))
    info_2.config(text=(
        f'\nPlayer: {player_2[0:10]}\n' +
        f'Score: {score_2}\n' +
        f'Lives: {lives_2}'
    ))
    info_1.place(x=50, y=game_area_height + 50)
    info_2.place(x=game_area_width - 100, y=game_area_height + 50)
    if game_over_message != '':
        message = Label(win, style='Message.TLabel')
        message.config(text=game_over_message)
        message.place(y=200, x=100, width=game_area_width - 200)


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

# handler for network messages


def on_network_message(timestamp, user, message):
    if user == 'system':
        channel_user(user, message)
    # key_downs (only of interest to the server)
    global keys_down_me, keys_down_opponent
    if game_state['is_server']:
        if user == game_state['me'] and type(message) is list:
            keys_down_me = set(message)
        if user == game_state['opponent'] and type(message) is list:
            keys_down_opponent = set(message)
    # shared state (only of interest to the none-server)
    if type(message) is dict and not game_state['is_server']:
        game_state['shared'] = message
        redraw_screen()

# track_image = ImageTk.PhotoImage(Image.open('image/race_track.png'))
# track_frame = canvas.create_image(0, 0, anchor=NW, image=track_image)


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
    y = -15
    canvas.move(car1_frame, x, y)
    car1_track_boundary('self')
    obstacle_boundary()


def down(e):
    x = 0
    y = 15
    canvas.move(car1_frame, x, y)
    car1_track_boundary('self')
    obstacle_boundary()


def up2(e):
    x = 0
    y = -15
    canvas.move(car2_frame, x, y)
    car2_track_boundary('self')


def down2(e):
    x = 0
    y = 15
    canvas.move(car2_frame, x, y)
    car2_track_boundary('self')


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


def win_condition():
    car1_edge = canvas.bbox(car1_frame)
    car2_edge = canvas.bbox(car2_frame)
    win_edge = canvas.bbox(win_line2)


def game_loop():
    while True:
        track_scroll()
        win_condition()
        if time.time() > end_time:
            break


# start - before game loop
def start():
    game_state['me'] = simpledialog.askstring(
        'Input', 'Your user name', parent=win)
    channel = simpledialog.askstring(
        'Input', 'Channel', parent=win)
    connect(channel, game_state['me'], on_network_message)
    message.config(text='Waiting for an opponent...')
    message.place(y=200, x=100, width=track_frame - 200)
    # wait for an opponent
    while game_state['opponent'] == None:
        tk_sleep(win, 1 / 10)
    track_frame.destroy()
    # start game loop if i am the server
    if game_state['is_server']:
        game_loop()


game_loop()
win.mainloop()
