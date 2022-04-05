from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_puddle()

    if ball.xcor() < -410:
        scoreboard.r_point()
        ball.reset()

    if ball.xcor() > 410:
        scoreboard.l_point()
        ball.reset()

screen.exitonclick()
