from tkinter import *
import os
import random
import time
def addsquare(x, y):
    x = x+128
    y = y+128
    canvas.create_rectangle(x,y,x+8,y+8)
    root.update()


root = Tk()
size = 1024
canvas = Canvas(root, width = size, height = size)
canvas.pack()
x = 0
y = 0