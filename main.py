from turtle import Turtle, Screen
from random import randint

tim = Turtle()

tim.shape('turtle')

#for _ in range(4):
#    tim.forward(100)
#    tim.right(90)

# for num in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = ["red", "blue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    tim.color(colors[randint(0, len(colors)-1)])
    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)


for num_side_n in range(3, 11):
    draw_shape(num_side_n)

screen = Screen()
screen.exitonclick()
