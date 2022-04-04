import turtle as t
import random


# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for _ in colors:
#     rgb_colors.append((_.rgb.r, _.rgb.g, _.rgb.b))
# print(rgb_colors)
t.colormode(255)
num_row = 10
num_column = 10
starting_x = -250
starting_y = -200
unit = 50
dot_size = 20
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

turtle = t.Turtle()
turtle.speed("fastest")
turtle.hideturtle()

for i in range(num_column):
    x = starting_x
    y = starting_y + (unit * i)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    for j in range(num_row):
        turtle.dot(dot_size, random.choice(color_list))
        turtle.penup()
        turtle.forward(unit)
        turtle.pendown()


screen = t.Screen()
screen.exitonclick()
