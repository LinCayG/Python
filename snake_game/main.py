from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height =600)
screen.bgcolor("black") #sets background color of screen
screen.title("The Snake Game") #Put the title on the top of the screen
screen.tracer(0) #turns off the animation/screen refresh

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() #the program will start looking for keystrokes below
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()  # refreshes the screen and makes it appear that the all pieces of the snake move together
    time.sleep(0.1) #delays the refresh of the screen 0.1 seconds
    snake.move()

    #detect collision with food - use distance method from turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]: #checks head position but slices list to not check the head against the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
