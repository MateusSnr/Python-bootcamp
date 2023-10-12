from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(right_paddle.go_up, "i")
screen.onkey(right_paddle.go_down, "k")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()

