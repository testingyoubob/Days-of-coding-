from helper import *

t= turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')

colors = ["#ff3366", "#33ccff", "#33ff99", "#ffcc00"]
t.speed(0)
t.width(2)

for i in range(120):
    t.pencolor(colors[i % 4])
    t.forward(i * 3)
    t.left(91)  # 91 degrees creates a continuous twisting offset

screen.exitonclick()