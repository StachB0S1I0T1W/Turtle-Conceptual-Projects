from turtle import Turtle
import random

CARS_COLORS = ['black','orange','red','blue','green','yellow']
CARS_WIDTH = 1
CARS_LENGTH = 2
CARS_X_POSITION = 300

class CarsGenerator(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=CARS_WIDTH, stretch_len=CARS_LENGTH)
        self.penup()
    def generate_random_car(self):
        self.penup()
        self.goto(CARS_X_POSITION, random.randrange(-250, 250, 10))
    def forward_the_car(self):
        self.setheading(0)
        self.forward(10)
