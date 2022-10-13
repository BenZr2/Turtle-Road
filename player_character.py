from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_player()

    def reset_player(self):
        self.goto(0, -230)

    def move_forward(self):
        self.goto(self.pos()[0], self.pos()[1] + 10)

    def move_backward(self):
        self.goto(self.pos()[0], self.pos()[1] - 10)

    def check_crossing_street(self):
        if self.pos()[1] > 200:
            self.reset_player()
            return True
