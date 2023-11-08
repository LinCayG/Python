from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rtpaddle = Paddle((350, 0))
ltpaddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(rtpaddle.go_up, "Up")
screen.onkey(rtpaddle.go_down,"Down")

screen.onkey(ltpaddle.go_up, "w")
screen.onkey(ltpaddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280: #detecting collision with wall
        ball.bounce_y()

    # detecting collision with right and left paddle
    if ball.distance(rtpaddle) < 50 and ball.xcor() > 320 or ball.distance(ltpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when R Paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when L Paddle Misses
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
