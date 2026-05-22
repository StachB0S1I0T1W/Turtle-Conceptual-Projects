from turtle import Turtle

class ScoreCounter(Turtle):
    def __init__(self):
        super().__init__()
        self.level_number = 1
    def level_number_write(self):
        self.penup()
        self.goto(-290,270)
        self.color('black')
        self.write(f"Level {self.level_number}",align="left",font=("Arial",15,"normal"))
        self.hideturtle()
    def next_level(self):
        self.clear()
        self.level_number += 1
        self.color("black")
        self.write(f"Level {self.level_number}",align="left",font=("Arial", 15,"normal"))
        self.hideturtle()
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"GAME OVER\nYour highest level is {self.level_number}",align="center",font=("Comic Sans",24,"normal"))
        self.hideturtle()