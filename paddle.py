from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.color("gray")
        self.shape("square")
        self.turtlesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.goto(x=x,y=0)

    def move_up(self):
        if self.ycor() > 230:
            pass
        else:
            self.setheading(90)
            self.forward(20)

    def move_down(self):
        if self.ycor() < -230:
            pass
        else:
            self.setheading(270)
            self.forward(20)

        