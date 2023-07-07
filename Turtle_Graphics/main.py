import turtle as t
import random

tim = t.Turtle() #creates a turtle object to use
tim.shape("turtle")
tim.color("teal")

for _ in range(4): #draws a square
    tim.forward(100)
    tim.right(90)

for length in range(15): #draws a dashed line
    tim.forward(5)
    tim.pu()
    tim.forward(5)
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

t.colormode(255) #changes the colormode for the Turtle module
def random_color(): #will generate a random color using rgb
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_colors = (r, g, b)
    return my_colors
#Creating a random walk
directions = [0, 90, 180, 270] #directions that the turtle can go
tim.pensize(20) #sets the thickness of the line
tim.speed("fastest") #sets the speed for the turtle to draw
for _ in range(200):
    tim.color(random_color()) #assigns the color from the random_color function
    tim.forward(30)
    tim.setheading(random.choice(directions)) #Turtle will walk randomly 30 steps




screen = t.Screen() #creates screen for the Turtle
screen.exitonclick() #Keeps the screen on until we click it