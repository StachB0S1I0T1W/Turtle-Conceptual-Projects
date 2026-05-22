from turtle import Turtle,Screen
import turtle_player
from cars_generator import CarsGenerator
from score_counter import ScoreCounter
import time

turtle_crossing_screen = Screen()
turtle_crossing_screen.setup(width=600,height=600)
turtle_crossing_screen.bgcolor('white')
turtle_crossing_screen.title("The Turtle Crossing Game")
turtle_crossing_screen.tracer(0)

color_of_turtle = turtle_crossing_screen.textinput("Turtle Crossing","Welcome to the Turtle Crossing game!\nPlease enter the color you want your little guy to have (Black/Orange/Red/Blue/Green/Yellow):\n")
while color_of_turtle not in turtle_player.TURTLE_COLORS:
    color_of_turtle = turtle_crossing_screen.textinput("Error!","Invalid color name!\nPlease try again (Black/Orange/Red/Blue/Green/Yellow):\n")
turtle_player = turtle_player.TurtlePlayer(color_of_turtle)
turtle_player.set_turtle_player()
turtle_player.move_forward()
turtle_crossing_screen.listen()
turtle_crossing_screen.onkey(turtle_player.move_forward, 'w')
turtle_crossing_screen.onkey(turtle_player.move_forward, 'Up')

cars = CarsGenerator()
score_count = ScoreCounter()
score_count.level_number_write()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    turtle_crossing_screen.update()
    cars.generate_random_car()
    cars.forward_the_car()
    score_count.level_number_write()
    if turtle_player.ycor() == 280:
        score_count.next_level()
        turtle_player.set_turtle_player()

turtle_crossing_screen.exitonclick()
