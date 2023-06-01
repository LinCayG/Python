from turtle import Turtle, Screen
import random

tim = Turtle() #creates a turtle object to use
tim.shape("turtle")
tim.color("teal")

for _ in range(4): #draws a square
    tim.forward(100)
    tim.right(90)

for length in range(15): #draws a dashed line
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()

#Drawing various shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

colors = ["light steel blue","sienna", "spring green", "red", "indigo", "dark green", "gold", "aquamarine", "black"]

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)







screen = Screen() #creates screen for the Turtle
screen.exitonclick() #Keeps the screen on until we click it