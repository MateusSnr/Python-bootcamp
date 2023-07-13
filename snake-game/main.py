import turtle
from turtle import Screen, Turtle

turtle.colormode(255)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(51, 102, 0)
screen.title("snake game")

teste = Turtle()

bg_color_1 = Turtle("square")
bg_color_1.color(64, 128, 0)
bg_color_1.shapesize(25, 30, 1)

bg_color_2 = Turtle("square")
bg_color_2.color(64, 128, 0)
bg_color_2.penup()
bg_color_2.setpos(0, -260)
bg_color_2.pendown()
bg_color_2.shapesize(4, 30)

def change_color(bg):
    bg.color(217, 255, 102)

for x in range(-260, 260, 20):
    bg_color_3 = Turtle("square")
    bg_color_3.color(153, 204, 0)
    bg_color_3.penup()
    bg_color_3.setpos(x, 210)
    change_color(bg_color_3)

segment_1 = Turtle("square")
segment_1.color(51, 102, 255)

segment_2 = Turtle("square")
segment_2.color(51, 102, 255)

segment_3 = Turtle("square")
segment_3.color(51, 102, 255)

screen.exitonclick()