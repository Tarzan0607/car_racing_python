import tkinter as tk
import time
import random
from network import connect, send
from tkinter import *
from tkinter.ttk import Label
from PIL import Image, ImageTk
from tk_sleep import tk_sleep
from tkinter import simpledialog, PhotoImage, Frame, messagebox
from window_handler import load_window, start_window_loop
from random import randint


win = tk.Tk()
win.geometry('1600x900')  # set window size
win.resizable(False, False)  # fix window
message = Label(win, style='Message.TLabel')
info_1 = Label(win)
info_2 = Label(win)
obstacle_item = None
boost_item = None
win_line2 = None
#car1_right = None
#car2_right = None
end_time = time.time() + 18
end_time1 = time.time() + 22


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


# some initial variables including a game state
# (tidy to keep everything in a dictionary
game_state = {
    'me': None,
    'opponent': None,
    'is_server': None,
    'shared': {
        'car1_x': '',
        'car1_y': 200,
        'car2_x': '',
        'car2_y': 600,
        'obstacle_x': '',
        'obstacle_y': '',
        'boost_x': '',
        'boost_y': '',
        'game_over_message': ''
    }
}


def create_obstacle_item():
    global obstacle_item
    obstacle_item = canvas.create_image(
        1600, random.randint(150, 750), image=obstacle_image1)
    return obstacle_item


def create_boost_item():
    global boost_item
    boost_item = canvas.create_image(
        1600, random.randint(150, 750), image=boost_image1)
    return boost_item


def create_win_line2():
    global win_line2
    win_line2 = canvas.create_image(1600, 450, image=win_line1)
    print('creating win line')
    return win_line2


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


'''
def car1_boundary(self):
    car1_edge = canvas.bbox(car1_frame)
    car1_left = car1_edge[0]
    car1_top = car1_edge[1]
    car1_right = car1_edge[2]
    car1_bottom = car1_edge[3]


def car2_boundary(self):
    car2_edge = canvas.bbox(car2_frame)
    car2_left = car2_edge[0]
    car2_top = car2_edge[1]
    car2_right = car2_edge[2]
    car2_bottom = car2_edge[3]
'''


def boost_boundary():
    car1_edge = canvas.bbox(car1_frame)
    car2_edge = canvas.bbox(car2_frame)
    boost_edge = canvas.bbox(boost_item)
    if boost_edge[0] < car1_edge[2] and (boost_edge[1] - 45) < car1_edge[1] < (boost_edge[3] + 45):
        canvas.move(car1_frame, 50, 0)
        canvas.delete(boost_item)
        print('boost!')
        create_boost_item()
    if (boost_edge[0] - 35) < car2_edge[2] and (boost_edge[1] - 45) < car2_edge[1] < (boost_edge[3] + 45):
        canvas.move(car2_frame, 50, 0)
        canvas.delete(boost_item)
        print('boost!')
        create_boost_item()
    if boost_edge[2] < -50:
        canvas.delete(boost_item)
        print('deleting boost')
        create_boost_item()


def obstacle_boundary():
    car1_edge = canvas.bbox(car1_frame)
    car2_edge = canvas.bbox(car2_frame)
    obstacle_edge = canvas.bbox(obstacle_item)
    if obstacle_edge[0] < car1_edge[2] and (obstacle_edge[1] - 45) < car1_edge[1] < (obstacle_edge[3] + 45):
        canvas.move(car1_frame, -50, 0)
        canvas.delete(obstacle_item)
        print('obstacle collision')
        create_obstacle_item()
    if obstacle_edge[0] < car2_edge[2] and (obstacle_edge[1] - 45) < car2_edge[1] < (obstacle_edge[3] + 45):
        canvas.move(car2_frame, -50, 0)
        canvas.delete(obstacle_item)
        print('obstacle collision')
        create_obstacle_item()
    if obstacle_edge[2] < -50:
        canvas.delete(obstacle_item)
        print('deleting obstacle')
        create_obstacle_item()


def win_condition():
    car1_edge = canvas.bbox(car1_frame)
    car1_right = car1_edge[2]
    car2_edge = canvas.bbox(car2_frame)
    car2_right = car2_edge[2]
    win_line_edge = canvas.bbox(win_line2)
    win_line_left = win_line_edge[0]
    if car1_right > win_line_left:
        messagebox.showinfo('Red car wins!', 'Red car wins!')
    if car2_right > win_line_left:
        messagebox.showinfo('Blue car wins!', 'Blue car wins!')
    if car1_right and car2_right > win_line_left:
        messagebox.showinfo("It's a tie", "It's a tie")


def get_opponent_and_decide_game_runner(user, message):
    # who is the server (= the creator of the channel)
    if 'created the channel' in message:
        name = message.split("'")[1]
        game_state['is_server'] = name == game_state['me']
    # who is the opponent (= the one that joined that is not me)
    if 'joined channel' in message:
        name = message.split(' ')[1]
        if name != game_state['me']:
            game_state['opponent'] = name


def on_network_message(timestamp, user, message):
    if user == 'system':
        get_opponent_and_decide_game_runner(user, message)
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
# handler for network messages

# Draw the elements (cars, obstacle , boost) on the screen


def redraw_screen():
    car1_x, car1_y, car2_x, car2_y, obstacle_x, obstacle_y, boost_x, boost_y, \
        game_over_message =\
        game_state['shared'].values()
    car1_frame.place(x=(car1_x + 150), y=car1_y)
    car2_frame.place(x=(car2_x + 150), y=car2_y)
    obstacle_image1.place(x=obstacle_x, y=obstacle_y)
    boost_image1.place(x=boost_x, y=boost_y)
    if game_over_message != '':
        message = Label(win, style='Message.TLabel')
        message.config(text=game_over_message)
        message.place(y=200, x=100, width=win - 200)


def up(e):
    x = 0
    y = -15
    canvas.move(car1_frame, x, y)
    car1_track_boundary('self')
    obstacle_boundary()
    on_key_down(2300)


def down(e):
    x = 0
    y = 15
    canvas.move(car1_frame, x, y)
    car1_track_boundary('self')
    obstacle_boundary()
    on_key_down(2302)


def up2(e):
    x = 0
    y = -15
    canvas.move(car2_frame, x, y)
    car2_track_boundary('self')
    boost_boundary()


def down2(e):
    x = 0
    y = 15
    canvas.move(car2_frame, x, y)
    car2_track_boundary('self')
    boost_boundary()


def on_key_down(keycode):
    global last_down
    last_down = keycode
    if keycode in keys_down:
        return
    print('network press down')
    # add key that is down to keys_down
    keys_down.add(keycode)
    send(list(keys_down))  # send keys down via network


def on_key_up(keycode):
    global last_down
    # ignore false release / auto-repeat
    # (a release that is followed by a down in
    # in less than 0.01 seconds is considered false)
    last_down = None
    tk_sleep(win, 1 / 1000)
    if last_down == keycode:
        return
    if keycode not in keys_down:
        return
    print('network press release')
    # remove key that is relased from keys_down
    keycode in keys_down and keys_down.remove(keycode)
    send(list(keys_down))  # send keys down via network


keys_down_me = set()
keys_down_opponent = set()
keys_down = set()  # locally
last_down = None

win.bind('<Up>', up)
win.bind('<KeyRelease-Up>', lambda e: on_key_up(2300))
win.bind('<Down>', down, lambda e: on_key_down(2302))
win.bind('<KeyRelease-Down>', down, lambda e: on_key_up(2302))
win.bind("<w>", up2)
win.bind("<s>", down2)


def game_loop():
    shared = game_state['shared']
    car1_x, car1_y, car2_x, car2_y, obstacle_x, obstacle_y, boost_x, boost_y = list(
        shared.values())[0:8]
    shared['player_1'] = game_state['me']
    shared['player_2'] = game_state['opponent']
    while True:
        tk_sleep(win, 1/30)
        canvas.move(track_frame, -25, 0)
        # canvas.bbox(ALL)
        if obstacle_item is None:
            create_obstacle_item()
        if obstacle_item is not None:
            canvas.move(obstacle_item, -35, 0)
            obstacle_boundary()
        if boost_item is None:
            create_boost_item()
        if boost_item is not None:
            canvas.move(boost_item, -35, 0)
            boost_boundary()
        if time.time() > end_time and win_line2 is None:
            create_win_line2()
        if win_line2 is not None:
            canvas.move(win_line2, -25, 0)
            win_condition()
        if 38 in keys_down_me:
            up()
        if 40 in keys_down_me:
            down()
        if 38 in keys_down_opponent:
            up2()
        if 40 in keys_down_opponent:
            down2()
        if time.time() > end_time1:
            break
        shared['car1_x'] = car1_x
        shared['car1_y'] = car1_y
        shared['car2_x'] = car2_x
        shared['car1_y'] = car2_y
        shared['obstacle_x'] = obstacle_x
        shared['obstacle_y'] = obstacle_y
        shared['boost_x'] = boost_x
        shared['boost_y'] = boost_y
        send(game_state['shared'])
        # redraw_screen()
        if shared['game_over_message'] != '':
            break


game_loop()
win.mainloop(win)
