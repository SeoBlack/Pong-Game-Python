from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
paddle = Paddle(380)
paddle2 = Paddle(-380)
ball = Ball()
score = ScoreBoard()
screen.listen()
screen.onkeypress(fun=paddle.move_up , key="Up")
screen.onkeypress(fun=paddle.move_down , key="Down")
screen.onkeypress(fun=paddle2.move_up , key="w")
screen.onkeypress(fun=paddle2.move_down , key="s")
keep = True

while keep:

    screen.update()
    ball.move()
    time.sleep(ball.ballspeed)
    #detect collision with upper and lower walls.
    if ball.ycor() >= 288 or ball.ycor() <= -281:
        ball.bounce_y()
    #detect collision with paddles
    if ball.distance(paddle) < 50 and ball.xcor() > 350 or  ball.distance(paddle2) < 50 and ball.xcor() < -350:
        ball.bounce_x()



    #detect collision with left wall.
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_score_player_1()
        score.update_scoreboard()
        speed = 0.01
    #detect collision with right wall
    if ball.xcor() < -380:

        ball.reset_position()
        score.increase_score_player_2()
        score.update_scoreboard()







screen.exitonclick()