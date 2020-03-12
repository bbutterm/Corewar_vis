from tkinter import *
import os
import random
import time
from tkinter import Tk, Canvas, Frame, BOTH
def recost(coords):
    ret = []
    x = coords//64
    y = round(coords/64)
    ret.append(x)
    ret.append(y)
    return ret
def addsquare(x, y, color):
    x = x+128
    y = y+128
    canvas.create_rectangle(x,y,x+8,y+8,fill = color)
    root.update()

root = Tk()
root.geometry("1024x1024")
size = 769
canvas = Canvas(root, width = 1280, height = 1280)
# canvas.place(anchor = NE)
canvas.pack()
img = PhotoImage(file = "Unknown1.png")
canvas.create_image(511, 510,image = img,anchor = CENTER)
y = 0
x = 0
while (x < 769):
    color = random.choice(['red', 'blue'])
    addsquare(x,y,color)
    x+=12
    if x == 768:
        x = 0
        y += 12
    if y == 768:
        time.sleep(3000)
        break
root.mainloop()

