from tkinter import *
import time

root = Tk()
# Setting window size instead of usin canvas to do that
root.geometry('800x600')
pos = 0

background_image = PhotoImage(file="image/full_track.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0)

image_list = []     # List for holding references to labels with images


def addImages(files):
    for f in files:
        image = PhotoImage(file=f)
        label = Label(root, image=image)
        label.image = image    # Remember the image outside the function
        label.place(x=files[f][0], y=files[f][1])
        image_list.append(label)    # Append created Label to the list


def move(xPos):
    pos = background_label.winfo_x() - xPos
    while background_label.winfo_x() > pos:
        background_label.place(x=background_label.winfo_x()-1)
        for image in image_list:    # Loop over labels in list
            image.place(x=image.winfo_x()-1)    # Move the label
        root.update()
        time.sleep(0.001)


img = {"tesla.png": [10, 10], "track.png": [50, 50]}
addImages(img)

root.after(1000, move, 5000)  # Waits 1 second and then moves images
# root.after(2000, move, 300)  # Waits 1 second and then moves images
# root.after(3000, move, 300)  # Waits 1 second and then moves images


root.mainloop()
