from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height =600)
screen.bgcolor("black") #sets background color of screen
screen.title("The Snake Game") #Put the title on the top of the screen
screen.tracer(0) #turns off the animation/screen refresh

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()  # refreshes the screen and makes it appear that the all pieces of the snake move together
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
