import turtle
from turtle import Turtle, Screen
from random import random, choice
import colorgram

tim = Turtle()
##tim.penup()
##tim.setposition(-50, 300)
##tim.pendown()
tim.shape("turtle")
'''
def draw_turtle(edges):
    R = random()
    B = random()
    G = random()
    tim.color(R, G, B)
    angle = 360 / edges
    for i in range(edges):
        for j in range(13):
            tim.pendown()
            tim.forward(10)
            tim.penup()
            tim.forward(2)
        tim.right(angle)


for i in range(3, 14):
    draw_turtle(i)
'''


## plot sequence of circles
def turtle_color():
    R = random()
    B = random()
    G = random()
    return tim.color(R, G, B)
'''
tim.speed(0)
deviation = 5
numbers = int(360/deviation)
for i in range(numbers):
    turtle_color()
    tim.circle(100)
    tim.left(deviation)
'''

### Hirst crazy dot painting

# Take color out of picture
colors = colorgram.extract('crazy_art.jpg', 30)
all_colors = [(x.rgb.r,x.rgb.g,x.rgb.b) for x in colors]
all_colors = all_colors[4:]
turtle.colormode(255)
tim.hideturtle()
tim.speed(0)
init_x = -300
init_y = -300
for i in range(10):
    tim.penup()
    tim.setposition(init_x,init_y + 50*i)
    tim.pendown()
    for j in range(10):
        my_color = choice(all_colors)
        tim.dot(20, my_color)
        tim.penup()
        tim.forward(50)
        tim.pendown()

screen = Screen()
screen.exitonclick()
