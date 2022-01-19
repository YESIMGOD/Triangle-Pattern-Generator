from tkinter import N
import turtle
import colorsys

tu=turtle.Turtle()
sc=turtle.Screen()
sc.bgcolor('black')
tu.speed(0)
n=500
h=0
for i in range (360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    tu.color(c)
    for j in range (2):
        tu.left(250)
        tu.forward(i*3)
        tu.left(2)
        tu.forward(2)