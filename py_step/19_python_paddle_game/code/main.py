from turtle import Screen;
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.title('Paddle-Game')
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()

screen = Screen()
screen.listen()
screen.onkey(paddle1.go_up, 'Up')
screen.onkey(paddle1.go_down, 'Down')
screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle2.go_down, 's')


game_is_on = True

while game_is_on :
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce()


screen.exitonclick()