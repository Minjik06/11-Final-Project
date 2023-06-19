import tkinter as tk
from typing import Text
import numpy as np
import csv
from PIL import ImageTk,Image
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("950x530")
w.attributes('-topmost',True)
c = tk.Canvas(height=530,width=950,bg="#ffdddd")
c.pack()
f=open('map1.txt')
map1=f.readlines()


walls=[]
img22 = [[]]
k=0
p=0
for i in range(1,2):
    for i in range(len(map1)):
        print(map1[i])
        p=0
        k+=30
        for j in range(len(map1[i])):
            p+=30
            if map1[i][j]=="*":
                print(f"map1: {j},{i}")
                c.create_rectangle(j+p,i+k,j+p+30,i+k+30, fill='green')

def getImage(x,y):
    img = Image.open("assets/skt.png").convert("RGBA")
    xi = x*32
    yi = y*48
    img3 = img.crop([xi,yi,xi+32,yi+48])
    return ImageTk.PhotoImage(img3)


#img = tk.PhotoImage(file="assets/tiles.png")
wall=[]
img = [[]]
wall.append(getImage(7,4))
wall.append(getImage(7,5))
wall.append(getImage(7,6))
wall.append(getImage(7,7))
j=c.create_image(7*32,4*48,image=wall[0])
img.append(j)



def keyPress(e):
    global k
    for i in range(1,2):
        for i in range(len(map1)):
            print(map1[i])
            p=0
            k+=30
            for j in range(len(map1[i])):
                p+=30
                if map1[i][j]=="*":
                    print(f"map1: {j},{i}")
                else:
                    print(e)
                    print(e.keycode, e.keysym, e.x, e.y)
                    x=5
                    y=0
                    if e.keysym=="Left":
                        c.itemconfig(img,image=wall[1])
                        c.move(j,-1*x,y)
                    if e.keysym=="Right":
                        c.itemconfig(img,image=wall[2])
                        c.move(j,x,y)
                    if e.keysym=="Up":
                        c.itemconfig(img,image=wall[3])
                        c.move(j,y,-1*x)
                    if e.keysym=="Down":
                        c.itemconfig(img,image=wall[0])
                        c.move(j,y,x)
                w.bind("<Left>",keyPress)
                w.bind("<Right>",keyPress)
                w.bind("<Up>",keyPress)
                w.bind("<Down>",keyPress)

w.mainloop()