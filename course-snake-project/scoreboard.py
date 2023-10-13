from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.contents = 0
        self.data = "data.txt"
        self.high_score = int(self.read_high_score_data())
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def read_high_score_data(self):
        with open(self.data) as file:
            self.contents = file.read()
        return self.contents

    def write_high_score_data(self, new_high_score):
        with open(self.data, mode="w") as file:
            file.write(str(new_high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_data(self.high_score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #   self.goto(0,0)
    #   self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)