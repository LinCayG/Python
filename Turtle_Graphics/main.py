from turtle import Turtle, Screen

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









screen = Screen() #creates screen for the Turtle
screen.exitonclick() #Keeps the screen on until we click it