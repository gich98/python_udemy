import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_is_on = True
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=player.move)

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.end_road():
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
