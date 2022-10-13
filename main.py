from turtle import Turtle, Screen
from player_character import Player
from entity import Car
from level_display import LevelDisplay, Curb
import time


screen = Screen()
screen.setup(500, 500)
screen.listen()
screen.tracer(0)

fred = Player()
level_display = LevelDisplay()
curb = Curb()

cars = []
for i in range(15):
    cars.append(Car())

screen.onkeypress(fred.move_forward, "w")
screen.onkeypress(fred.move_backward, "s")


def speed_up_cars():
    for car in cars:
        car.increase_speed()


game_is_on = True

while game_is_on:
    time.sleep(0.001)
    if fred.check_crossing_street():
        level_display.level += 1
        level_display.draw()
        speed_up_cars()
    for car in cars:
        car.forward(car.speed)
        car.check_reset_need()
        if car.check_turtle_crash(fred):
            game_is_on = False
    screen.update()

screen.exitonclick()
