"""
NOTES
import turtle as t
import heroes

"""
import turtle
from turtle import Turtle, Screen
import random

teus_the_turtle = Turtle()
teus_the_turtle.shape("turtle")
teus_the_turtle.color("cyan1")

"""Challenge 1: draw a square
for i in range(4):
    teus_the_turtle.right(90)
    teus_the_turtle.forward(100)
"""

"""Challenge 2: draw a dashed line
for i in range(9):
    teus_the_turtle.forward(5)
    teus_the_turtle.penup()
    teus_the_turtle.forward(5)
    teus_the_turtle.pendown()
"""

"""Challenge 3: draw a triangle, square...
for number_of_sides in range (3,8):
    if number_of_sides == 3:
        angle = 360/number_of_sides
        for i in range(3):
            teus_the_turtle.forward(100)
            teus_the_turtle.right(angle)
    if number_of_sides == 4:
        angle = 360 / number_of_sides
        for i in range(4):
            teus_the_turtle.forward(100)
            teus_the_turtle.right(angle)
    if number_of_sides == 5:
        angle = 360 / number_of_sides
        for i in range(5):
            teus_the_turtle.forward(100)
            teus_the_turtle.right(angle)
    if number_of_sides == 6:
        angle = 360 / number_of_sides
        for i in range(6):
            teus_the_turtle.forward(100)
            teus_the_turtle.right(angle)
    if number_of_sides == 7:
        angle = 360 / number_of_sides
        for i in range(7):
            teus_the_turtle.forward(100)
            teus_the_turtle.right(angle)

OTHER WAY TO DO

colors = ["light slate gray", "royal blue", "cyan", "forest green", "pale goldenrod", "dark goldenrod", "magenta"]

def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        teus_the_turtle.forward(100)
        teus_the_turtle.right(angle)

for i in range(3,11):
    teus_the_turtle.color(random.choice(colors))
    draw_shape(i)
"""

"""Challenge 4: draw a random walk
colors = ["light slate gray", "royal blue", "cyan", "forest green", "pale goldenrod", "dark goldenrod", "magenta"]
directions = [0, 90, 180, 270]
teus_the_turtle.pensize(15)
teus_the_turtle.speed("fastest")

for i in range (200):
    teus_the_turtle.color(random.choice(colors))
    teus_the_turtle.forward(30)
    teus_the_turtle.setheading(random.choice(directions))
"""
#Random colors in RGB

turtle.colormode(255)
directions = [0, 90, 180, 270]
teus_the_turtle.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for i in range (200):
    teus_the_turtle.color(random_color())
    teus_the_turtle.forward(30)
    teus_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()