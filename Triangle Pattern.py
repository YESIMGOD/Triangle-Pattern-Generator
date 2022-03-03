from tkinter import N  #tkinter - Framework for creating GUI based elements.
import turtle          #turtle - Module providing drawing board like featuers.
import colorsys        #colorsys - Module serving as a conversion function between RGB and other colors.

tu=turtle.Turtle()
sc=turtle.Screen()
sc.bgcolor('black')
tu.speed(0)
n=500
h=0

for i in range (360):
    col=colorsys.hsv_to_rgb(h,1,0.8)  #hsv = Hue Saturation and Vue
    h+=1/n
    tu.color(col)
    for j in range (2):
        tu.left(250)
        tu.forward(i*3)
        tu.left(2)
        tu.forward(2)
