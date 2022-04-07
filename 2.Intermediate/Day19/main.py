import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
winner = ""
winner_score = 0

for _ in range(0, len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[_])
    turtle.goto(x=-235, y=(-70 + (30 * _)))
    turtle_list.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            is_race_on = False
            if winner == "":
                winner = turtle.fillcolor()
                winner_score = turtle.xcor()
            elif turtle.xcor() > winner_score:
                winner = turtle.fillcolor()
                winner_score = turtle.xcor()

if user_bet == winner:
    print(f"You got it! The winner is {winner}!!!")
else:
    print(f"The winner is {winner}. Oh no! The {user_bet} turtle lost...")

screen.exitonclick()
