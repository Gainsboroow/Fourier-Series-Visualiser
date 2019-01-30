"""
Fourier Series Visualiser
Created by Gainsboroow 
Github : https://github.com/Gainsboroow
Github Repository : https://github.com/Gainsboroow/Fourier-Series-Visualiser
"""

from tkinter import *
from math import *

import random

height = 200
width = 500

window = Tk()
window.title("Fourier Series Visualiser")
window.geometry(str(width)+"x"+str(height)+"+0+0")

canvas = Canvas(window, bg = "black")
canvas.place(x=0,y=0, width = width, height = height)

centerX, centerY = 150, 100
startX = 300

angle = 0
points = []
aRefresh = []

circleNumber = 7
color = ["#"+("%06x"%random.randint(0,16777215)) for i in range(circleNumber)]

def nextStep():
    global angle
    for i in aRefresh:
        canvas.delete(i)
    aRefresh.clear()

    for i in points:
        canvas.move(i, 1, 0)

    nX, nY = centerX, centerY

    for i in range(circleNumber):
        n = 2*i + 1
        radius = 50 * 4 / (n*pi)
        aRefresh.append( canvas.create_oval(nX - radius, nY - radius, nX + radius, nY+ radius, outline = "chartreuse" ) )
        aRefresh.append( canvas.create_oval(nX - 2, nY - 2, nX + 2, nY + 2, fill = "red") )
        nX += radius * cos(n * angle)
        nY += radius * sin(n * angle)
        
    aRefresh.append( canvas.create_oval(nX - 2, nY - 2, nX + 2, nY + 2, fill = "red") )
    points.append( canvas.create_line(startX, nY, startX+1, nY+1, fill = "red") ) #Image
    
    aRefresh.append( canvas.create_oval(startX-3, nY-3, startX+3, nY+3, fill = "chartreuse") ) #boutLigne
    aRefresh.append( canvas.create_line(nX, nY, startX, nY, fill = "chartreuse") ) #Ligne reliant

    angle += 0.01
    canvas.after(1, nextStep)

    if len(points) > 1000:
        canvas.delete(points[0])
        points.pop(0)

nextStep()

window.mainloop()