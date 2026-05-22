from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
    def write_score(self):
        self.goto(0,260)
        self.color("white")
        self.write(f"Score: {self.score}",align="center", font=("Comic Sans", 24,"normal"))
        self.hideturtle()
    def clear_the_score(self):
        self.clear()
        self.score += 1
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Comic Sans", 24, "normal"))
        self.hideturtle()
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()