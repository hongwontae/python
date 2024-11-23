from turtle import Turtle, Screen;

tim = Turtle()
screen = Screen()

for _ in range(0,4) :
    tim.forward(100)
    tim.penup()
    tim.right(90)
    tim.pendown()



screen.exitonclick()