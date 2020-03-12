from tkinter import *
import os
import random
import time
from tkinter import Tk, Canvas, Frame, BOTH
class champion:
  x = 0
  y = 0
  num = 0
  color = []
  def __init__(self,num):
    self.num = num
    coords = num*1024
    s = recost(coords)
    self.x = s[0]
    self.y = s[1]
    self.color = choosecolor(num)
  def move(self,steps):
    point = self.x * 64 + self.y * 64 + steps
    new_coords = recost(point)
    x = new_coords[0]
    y = new_coords[1]
  def info(self):
    print(self.x, " ",self.y)
    print(self.num)
    print(self.color)
  def fill(self):
    addsquare(self.x,self.y,color = self.color)
def choosecolor(num):
  color = []
  if num == 0:
    color.append('red')
  elif num == 1:
    color.append('blue')
  elif num == 2:
    color.append('green')
  else:
    color.append('yellow')
  return color
def recost(coords):
  ret = []
  x = coords%64
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

