from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

tim.shape('turtle')
tim.color('#dd22dd')
tim.speed('fastest')

angle = [-100,-30, -10,10, 50, 90, 120, 140, 200]

for _ in range(0, 100) :
    tim.forward(10)
    tim.setheading(random.choice(angle))

screen.exitonclick()
