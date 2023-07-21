from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400) #allows you to set width and height of screen
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ypos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle") #creates the turtle object in the shape of a turtle
    new_turtle.color(colors[turtle_index]) #assigns each turtle a color
    new_turtle.penup()
    new_turtle.goto(x=-230, y=ypos[turtle_index]) #turtle goes to the starting point of the race in different y positions
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: #using 230 and not 250 because the turtle is 40 px wide
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()