from turtle import Turtle


class LevelDisplay(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.goto(-180, 220)
        self.draw()

    def draw(self):
        self.clear()
        self.write("Level " + str(self.level), align="center",
                   font=("Arial", 14, "normal"))


class Curb(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260, 200)
        self.pendown()
        self.forward(520)
        self.penup()
        self.goto(-260, -200)
        self.pendown()
        self.forward(520)
