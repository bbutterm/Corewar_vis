from tkinter import *
import os
import random
import time
from tkinter import Tk, Canvas, Frame, BOTH
#max y = 63 max x = 63 max coord = 3969
lifes = 4096
count = 4
class champion:
  x = 0
  y = 0
  num = 0
  karet = []
  color = []
  def __init__(self,num):
    global count
    self.num = num
    coords = num*(4096/count)
    s = recost(coords)
    self.x = s[0]
    self.y = s[1]
    self.color = choosecolor(num)
    self.create_karet()
  def create_karet(self):
    self.karet.append(karetka(self))
    """
  def move(self,steps):
    new_coords = recost(steps)
    self.x = new_coords[0]
    self.y = new_coords[1]
    """
  def info(self):
    print(self.x, " ",self.y)
    print(self.num)
    print(self.color)
  def fill(self):
    global lifes
    lifes-=1
    addsquare(self.x,self.y,color = self.color)
class karetka():
  parent = 0
  x = 0
  y = 0
  color = []
  def __init__(self,champion):
    self.parent = champion.num
    self.x = champion.x
    self.y = champion.y
    self.color = champion.color
  def info(self):
    print(self.x, " ",self.y)
    print(self.parent)
    print(self.color)
  def move(self,steps):
    new_coords = recost(steps)
    self.x = new_coords[0]
    self.y = new_coords[1]
  def fill(self):
    global lifes
    lifes-=1
    addsquare(self.x,self.y,color = self.color)
def initchamps(count):
  count = count-1
  champs = []
  while (count >= 0):
    champs.append(champion(count))
    count-=1
  print(len(champs), "champs has been initialized:)")
  champs.reverse()
  return champs
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
    x = coords%64*12
    y = coords//64*12
    print(round(4065 // 64))
    ret.append(x)
    ret.append(y)
    return ret
def addsquare(x, y, color):
    x = x+128
    y = y+128
    canvas.create_rectangle(x,y,x+8,y+8,fill = color)
    root.update()
#a = champion(0)
a = champion(1)
a.karet[0].info()

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
champs = initchamps(count)
champs[0].fill()
champs[0].move(64)
champs[0].info()
champs[0].fill()
champs[0].move(1024)
champs[0].info()
champs[0].fill()
time.sleep(3000)
root.mainloop()

