from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.width = 1
        self.height = 1
        self.x_position = 0
        self.y_position = 0
        self.new_x = self.xcor()
        self.new_y = self.ycor()
    def set_the_ball(self):
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=self.width, stretch_len=self.height)
        self.penup()
        self.setpos(self.x_position,self.y_position)
    def move_ball(self):
        self.new_x += 8
        self.new_y += 8
        if self.ycor() == 300:
            self.new_x += 8
            self.new_y -= 8
        elif self.ycor() == -300:
            return self.move_ball()
        self.goto(self.new_x, self.new_y)

