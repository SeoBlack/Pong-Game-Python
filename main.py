from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
paddle = Paddle(370)
paddle2 = Paddle(-380)
ball = Ball()
screen.listen()
screen.onkey(fun=paddle.move_up , key="Up")
screen.onkey(fun=paddle.move_down , key="Down")
screen.onkey(fun=paddle2.move_up , key="w")
screen.onkey(fun=paddle2.move_down , key="s")
keep = True
y = -2
x = 2
while keep:

    screen.update()
    #detect collision with upper and lower walls.
    if ball.ycor() >= 288:
        y = -2
    if ball.ycor() <= -281:
        y = 2
    #detect collision with paddles
    if ball.distance(paddle) < 50 and ball.xcor() > 350:
        x = -2
    if ball.distance(paddle2) < 50 and ball.xcor() <  -360:
        x = 2
    #detect collision with left and write walls.
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.gameover()
        keep = False
    ball.move(y,x)
    time.sleep(0.01)




screen.exitonclick()