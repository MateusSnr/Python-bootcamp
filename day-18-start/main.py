#notes
#import turtle as t
#import heroes
from turtle import Turtle, Screen

teus_the_turtle = Turtle()
teus_the_turtle.shape("turtle")
teus_the_turtle.color("cyan1")

for i in range(4):
    teus_the_turtle.right(90)
    teus_the_turtle.forward(100)



screen = Screen()
screen.exitonclick()