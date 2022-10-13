from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.spawn_x = list(range(260, 750, 2))
        self.spawn_y = list(range(-180, 180, 25))
        self.speed = 1
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(
            ["red", "green", "yellow", "blue", "purple", "orange"]))
        self.reset_car()

    def increase_speed(self):
        self.speed += 0.5

    def reset_car(self):
        self.goto(random.choice(self.spawn_x), random.choice(self.spawn_y))

    def check_reset_need(self):
        if self.pos()[0] < -260:
            self.reset_car()

    def check_turtle_crash(self, player):
        if self.distance(player) < 18:
            return True
