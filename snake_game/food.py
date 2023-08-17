from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__() #calls the superclass Turtle to inherit attributes and methods of Turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #results in a 10x10 circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # dont want to use 300 because it would appear to close to edge
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # puts the food in a random place
