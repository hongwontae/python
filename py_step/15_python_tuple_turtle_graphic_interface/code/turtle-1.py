from turtle import Turtle, Screen;

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('#123456')
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(120)

timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('#bbb333')

for _ in range(0, 4) :
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)




screen = Screen()
screen.exitonclick()