from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import pygame

def play_music():
    pygame.init()
    pygame.mixer.music.load("Super-Mario.mp3")
    pygame.mixer.music.play()
    pygame.event.wait(1)

play_music()

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.bgpic("back.gif")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with the apple
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
