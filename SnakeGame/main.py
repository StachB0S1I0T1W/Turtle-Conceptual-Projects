import time
import turtle
from turtle import Screen
from snake import Snake, COORDINATES
from food import Food
from scoreboard import Scoreboard
# Screen generation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# Character choice

snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake.initialize_snake()
scoreboard.write_score()
for x in range(4):
    if x == 3:
        print("GO!")
        break
    print(3-x)
    time.sleep(1)

screen.onkey(lambda: snake.move_in_directions(90), "Up")
screen.onkey(lambda: snake.move_in_directions(270), "Down")
screen.onkey(lambda: snake.move_in_directions(180), "Left")
screen.onkey(lambda: snake.move_in_directions(0), "Right")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.segments[0].distance(food) < 17.5:
        food.refresh()
        snake.extend_snake()
        scoreboard.clear_the_score()

    # for segment in COORDINATES:
    #     if segment == snake.segments[0]:
    #         pass
    #     elif snake.segments[0].distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    #         print(" ")
    #         print("-----------------------------------")
    #         print(" ")
    #         print("Game Over!")
    #         print(f"Your score is: {scoreboard.score}")

    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280) or (snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280):
        game_is_on = False
        scoreboard.game_over()
        print(" ")
        print("-----------------------------------")
        print(" ")
        print("Game Over!")
        print(f"Your score is: {scoreboard.score}")

screen.exitonclick()