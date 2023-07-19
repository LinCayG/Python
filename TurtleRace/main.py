from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500, height=400) #allows you to set width and height of screen
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color: ")

tim = Turtle()


screen.exitonclick()