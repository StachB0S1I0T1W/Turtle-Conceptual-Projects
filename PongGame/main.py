import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

pong_screen = Screen()
pong_screen.setup(width=800,height=600)
pong_screen.bgcolor("black")
pong_screen.title("The Complete Pong Game")
pong_screen.tracer(0)
paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
paddle1.set_up_paddle()
paddle2.set_up_paddle()
pong_screen.listen()
pong_screen.onkey(paddle1.go_up, "Up")
pong_screen.onkey(paddle1.go_down,"Down")
pong_screen.onkey(paddle2.go_up,"w")
pong_screen.onkey(paddle2.go_down,"s")
ball = Ball()
ball.set_the_ball()
ball.speed('slowest')
game_is_on = True
moving = 0
while game_is_on:
    time.sleep(0.08)  # Utilized in order to make the screen update itself with brief delays to make the ball go slower
    pong_screen.update()
    ball.move_ball()
pong_screen.exitonclick()