from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self,x_position,y_position):
        super().__init__()
        self.paddle = Turtle()
        self.width = 5
        self.height = 1
        self.x_position = x_position
        self.y_position = y_position
    def set_up_paddle(self):
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=self.width,stretch_len=self.height)
        self.paddle.penup()
        self.paddle.setpos(self.x_position, self.y_position)
    def go_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.penup()
        self.paddle.goto(self.paddle.xcor(),self.new_y)
    def go_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.penup()
        self.paddle.goto(self.paddle.xcor(), self.new_y)

