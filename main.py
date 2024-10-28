import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_left, "Left")
screen.onkey(turtle.move_right, "Right")
screen.onkey(turtle.move_down, "Down")

time_sleep = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()

    car_manager.create_car()
    car_manager.move_left()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() == 300:
        turtle.come_back_down()
        time_sleep = time_sleep/1.5
        scoreboard.level_up()


screen.exitonclick()


