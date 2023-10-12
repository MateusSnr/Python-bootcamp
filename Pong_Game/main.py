from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350,0),"red")
left_paddle = Paddle((-350,0), "green")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "i")
screen.onkey(right_paddle.go_down, "k")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -300:
        #needs to bounce
        ball.bounce_y()

    #Detecting collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detecting when the right_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    #Detecting when the left_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()

