from turtle import Turtle, Screen

tim = Turtle()
screen = Screen() #object that will control the window when the code is run

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear(): #will clear the screen and take the turtle back to the middle of the screen
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen() #tells the screen object to start listening for events

#this function is used as an input to this other fuction and will be triggered when the w is pressed on the keyboard;
#() is not used after move_forwards because the () indicates to trigger/call it now, but we want to triggered when the key is pressed
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick() #want the screen to stay until it is clicked, then it will disappear