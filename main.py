import tkinter as tk
import time
import tk_sleep
import random
from network import connect, send
from tkinter import *
from tkinter.ttk import Label
from PIL import Image, ImageTk
from tk_sleep import tk_sleep
from tkinter import simpledialog, PhotoImage, Frame
from window_handler import load_window, start_window_loop


win = tk.Tk()
win.geometry('1600x900')  # set window size
win.resizable(False, False)  # fix window
message = Label(win, style='Message.TLabel')
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


def obstacle_item():
    obstacle_item
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
    distance = (((boost_item.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
    if distance < (self.width + other.width)/2.0:
        canvas.move(car1_frame, 100, 0)
        canvas.delete('boost')
        print('collision')


def obstacle_boundary():
    car1_edge = canvas.bbox(car1_frame)
    car2_edge = canvas.bbox(car2_frame)
    obstacle_edge = canvas.bbox(obstacle_item)
    if obstacle_edge[0] < car1_edge[2] < obstacle_edge[2] and obstacle_edge[1] < car1_edge[1] < obstacle_edge[3]:
        canvas.move(car1_frame, 100, 0)
        canvas.delete(boost_item)
        print('collision')


# some initial variables including a game state
# (tidy to keep everything in a dictionary
game_state = {
    'me': None,
    'opponent': None,
    'is_server': None,
    'shared': {
        'car1_y': '',
        'car2_y': '',
        'obstacle_x': '',
        'boost_x': '',
        'game_over_message': ''
    }
}


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

# Draw the elements (car, obstacle , boost) on the screen


def redraw_screen():
    car1_y, car2_y, obstacle_x, boost_x,\
        game_over_message =\
        game_state['shared'].values()
    car1_frame.place(car1_y)
    car2_frame.place(car2_y)
    obstacle_image1.place(x=obstacle_x)
    boost_image1.place(x=boost_x)
    if game_over_message != '':
        message = Label(win, style='Message.TLabel')
        message.config(text=game_over_message)
        message.place(y=200, x=100, width=win - 200)


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


def on_key_down(keycode):
    global last_down
    last_down = keycode
    if keycode in keys_down:
        return
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
    # remove key that is relased from keys_down
    keycode in keys_down and keys_down.remove(keycode)
    send(list(keys_down))  # send keys down via network


keys_down_me = set()
keys_down_opponent = set()
keys_down = set()  # locally
last_down = None

win.bind('<Up>', lambda e: on_key_down(38))
win.bind('<KeyRelease-Up>', lambda e: on_key_up(38))
win.bind('<Down>', lambda e: on_key_down(40))
win.bind('<KeyRelease-Down>', lambda e: on_key_up(40))
win.bind("<w>", up2)
win.bind("<s>", down2)


def win_condition():
    car1_edge = canvas.bbox(car1_frame)
    car2_edge = canvas.bbox(car2_frame)
    win_edge = canvas.bbox(win_line2)


def game_loop():
    while True:
        tk_sleep(win, 1/60)
        track_move = canvas.move(track_frame, -15, 0)
        canvas.move(obstacle_item, -15, 0)
        boost_move = canvas.move(boost_item, -15, 0)
        win_line_move = canvas.move(win_line2, -15, 0)
        win_condition()
        if time.time() > end_time:
            break


def start():
    # hide some things initially
    ### j('.wait, .ball, .paddle-1, .paddle-2').hide()
    # show the content/body (hidden by css)
    # j('body').show()
    # connect to network
    game_state['me'] = simpledialog.askstring(
        'Input', 'Your user name', parent=canvas)
    # note: adding prefix so I don't disturb
    # other class mates / developers using the same
    # network library
    channel = 'swak_han' + simpledialog.askstring(
        'Input', 'Channel', parent=win)
    connect(channel, game_state['me'], on_network_message)
    message.config(text='Waiting for an opponent...')
    message.place(y=200, x=100, width=1600/2)
    # wait for an opponent
    while game_state['opponent'] == None:
        tk_sleep(win, 1 / 10)
    message.destroy()
    # start game loop if i am the server
    if game_state['is_server']:
        game_loop()


start()
game_loop()
win.mainloop(win)
