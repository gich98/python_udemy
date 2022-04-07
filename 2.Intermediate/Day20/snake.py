from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
STARTING_LENGTH = 3
DIRECTION = {
    "UP": 90,
    "DOWN": 270,
    "LEFT": 180,
    "RIGHT": 0,
}


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in STARTING_POSITIONS:
            self.add_segment(_)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            next_segment = self.segments[i - 1]
            self.segments[i].goto(x=next_segment.xcor(), y=next_segment.ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION["DOWN"]:
            self.head.setheading(DIRECTION["UP"])

    def down(self):
        if self.head.heading() != DIRECTION["UP"]:
            self.head.setheading(DIRECTION["DOWN"])

    def left(self):
        if self.head.heading() != DIRECTION["RIGHT"]:
            self.head.setheading(DIRECTION["LEFT"])

    def right(self):
        if self.head.heading() != DIRECTION["LEFT"]:
            self.head.setheading(DIRECTION["RIGHT"])
