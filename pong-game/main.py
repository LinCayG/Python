from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rtpaddle = Paddle((350, 0))
ltpaddle = Paddle((-350,0))



screen.listen()
screen.onkey(rtpaddle.go_up, "Up")
screen.onkey(rtpaddle.go_down,"Down")

screen.onkey(ltpaddle.go_up, "w")
screen.onkey(ltpaddle.go_down,"s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
