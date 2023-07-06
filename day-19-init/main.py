import turtle
from turtle import Turtle, Screen
"""
teus = Turtle(shape="turtle")
teus.color("blue")
teus.penup()
teus.goto(-230, y=-150)

teus = Turtle(shape="turtle")
teus.color("red")
teus.penup()
teus.goto(-230, y=-90)

teus = Turtle(shape="turtle")
teus.color("orange")
teus.penup()
teus.goto(-230, y=-30)

teus = Turtle(shape="turtle")
teus.color("yellow")
teus.penup()
teus.goto(-230, y=30)

teus = Turtle(shape="turtle")
teus.color("green")
teus.penup()
teus.goto(-230, y=90)

teus = Turtle(shape="turtle")
teus.color("purple")
teus.penup()
teus.goto(-230, y=150)
"""

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]

for i in range(0, 6):
    teus = Turtle(shape="turtle")
    teus.color(colors[i])
    teus.penup()
    teus.goto(-230, y=y_positions[i])

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle  will win the race? Enter a color: ")
screen.exitonclick()

"""
def move_forwards():
    teus.forward(10)

def move_backwards():
    teus.backward(10)

def move_left():
    new_heading = teus.heading() + 10
    teus.setheading(new_heading)

def move_right():
    new_heading = teus.heading() - 10
    teus.setheading(new_heading)

def clear():
    teus.clear()
    teus.penup()
    teus.home()
    teus.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
"""

