from turtle import Turtle

TURTLE_COLORS = ['black','orange','red','blue','green','yellow']
TURTLE_STARTING_POSITION = -280
TURTLE_MOVING_LENGTH = 10

class TurtlePlayer(Turtle):
    def __init__(self,colors):
        super().__init__()
        self.shape('turtle')
        self.color(colors)
        self.penup()
        self.setheading(90)
    def set_turtle_player(self):
        self.goto(0,TURTLE_STARTING_POSITION)
    def move_forward(self):
        self.forward(TURTLE_MOVING_LENGTH)






