from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height =600)
screen.bgcolor("black") #sets background color of screen
screen.title("The Snake Game") #Put the title on the top of the screen
screen.tracer(0) #turns off the animation/screen refresh

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
    new_segment=Turtle(shape = "square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()  # refreshes the screen and makes it appear that the all pieces of the snake move together
    time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1): #makes the pieces to appear to "follow" the first segment
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
