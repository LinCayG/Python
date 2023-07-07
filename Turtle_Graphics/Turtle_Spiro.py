import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color(): #will generate a random color using rgb
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_colors = (r, g, b)
    return my_colors

tim.speed("fastest")

def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100) #draws a circle with radius of 100
        tim.setheading(tim.heading() + size_of_gap) #takes the current heading and adds 10 to it

draw_spiro(5) #calls the function with a gap of 5

screen = t.Screen()
screen.exitonclick()

