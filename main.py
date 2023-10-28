import random
from turtle import Turtle,Screen
import turtle
color_list = [(177, 59, 36), (239, 224, 2), (2, 99, 76), (215, 63, 123), (130, 36, 20), (245, 231, 46)]

draw = Turtle()
step = 50
r=20
draw.hideturtle()
turtle.colormode(255)
draw.penup()
draw.goto(-250,-250)
draw.pendown()
for i in range(10):
    for j in range(10):
        draw.dot(r,random.choice(color_list))
        draw.penup()
        draw.fd(step)
        draw.pendown()
    draw.penup()
    draw.goto(-250,-250+step*(i+1))
    draw.pendown()
screen = Screen()
screen.exitonclick()