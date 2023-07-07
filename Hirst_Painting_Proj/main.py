#Color list from extracting the colors from the image
color_list = [(241, 233, 45), (195, 12, 35), (239, 41, 131), (224, 157, 67), (41, 83, 176), (44, 214, 69), (190, 71, 29), (33, 36, 157), (235, 228, 4), (73, 11, 46), (23, 148, 26), (199, 35, 81), (198, 15, 7), (230, 151, 9), (238, 56, 31), (56, 18, 11), (218, 135, 187), (71, 75, 218), (88, 210, 134), (82, 189, 221), (20, 16, 50), (240, 156, 209), (102, 232, 177), (14, 95, 63), (11, 210, 225), (90, 74, 13)]

import turtle as turtle_module
import random

#create a 10x10 spot and paint 100 dots
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup() #eliminates drawing a line as the turtle moves
tim.hideturtle() #hides the turtle
tim.setheading(225) #point turtle to move to lower corner
tim.forward(250) #move starting dot to lower corner
tim.setheading(0) #sets the direction back to 0

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list)) #creates a 20 size dot that will be a random color from the Hirst image previously extracted
    tim.forward(50)

    if dot_count % 10 == 0:
        #moves the turtle back to the beginning and up a line after finishing a line of dots
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
