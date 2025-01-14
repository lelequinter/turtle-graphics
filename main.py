from turtle import Turtle, Screen
from random import randint, choice

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

colors = ["red", "blue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "purple"]
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed('fastest')


def draw_shape(num_sides):
    angle = 360 / num_sides
    tim.color(choice(colors))
    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)


def random_walk():
    tim.color(choice(colors))
    tim.forward(40)
    tim.right(choice(directions))


for num_side_n in range(3, 100):
    # draw_shape(num_side_n)
    random_walk()


screen = Screen()
screen.exitonclick()
