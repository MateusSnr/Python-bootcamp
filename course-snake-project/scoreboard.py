from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_turtle = Turtle()
        self.score_turtle.write("Home = ", False, align="center")

    def add(self):
        self.score_turtle.clear()
        self.score_turtle.write("Home = 1", False, align="center")