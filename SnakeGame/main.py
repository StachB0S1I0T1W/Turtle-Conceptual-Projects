import time
from turtle import Screen
from snake import Snake
# Screen generation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Character choice

snake = Snake()
snake.initialize_snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()