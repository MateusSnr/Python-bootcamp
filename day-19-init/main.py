import random
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
screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle  will win the race? Enter a color: ")
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_Color = turtle.pencolor()
            if winning_Color == user_bet:
                print(f"You've won! The {winning_Color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_Color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

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

