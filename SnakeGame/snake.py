from turtle import Turtle

COORDINATES = [(0,0),(-20,0), (-40,0)]
COLORS = ['RED','YELLOW','BLUE','GREEN','PURPLE']
UP = True
DOWN = True
RIGHT = True
LEFT = True

class Snake:
    def __init__(self):
        self.segments = []
        self.choose_color = ''
        self.color_chosen = ''
        self.x_cor = 0
        self.y_cor = 0
    def initialize_snake(self):
        self.choose_color = input('Welcome to the Hungry Snake Game!!!\n\n[RED,YELLOW,BLUE,GREEN,PURPLE]\nChoose the color from above to participate: \n').upper()
        while self.choose_color not in COLORS:
            print("Sorry, wrong color name!\nPlease try again.")
            self.choose_color = input('Welcome to the Hungry Snake Game!!!\n\n[RED,YELLOW,BLUE,GREEN,PURPLE]\nChoose the color from above to participate: \n').upper()
        self.color_chosen = self.choose_color.lower()
        for position in COORDINATES:
            self.add_segments(position) # Appends the parts of the snake to a special list

    def add_segments(self, position):
        self.snake = Turtle("square")
        self.snake.shape('square')
        self.snake.color(f'{self.color_chosen}')
        self.snake.penup()
        self.snake.goto(position)
        self.segments.append(self.snake)

    def extend_snake(self):
        self.add_segments(self.segments[-1].position()) # Extends the snake whenever it touches the food

    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.x_cor = self.segments[segment - 1].xcor()
            self.y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(self.x_cor, self.y_cor)
        self.segments[0].forward(20)
    def move_in_directions(self, direction):
        if (self.segments[0].heading() + 180) % 360 != direction:
            self.segments[0].setheading(direction)