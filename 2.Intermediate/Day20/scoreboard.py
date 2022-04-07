from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.read_highest_score()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def read_highest_score(self):
        with open("data.txt") as data:
            self.highest_score = int(data.read())

    def write_highest_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.highest_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.write_highest_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
