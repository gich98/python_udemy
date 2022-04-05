from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)






