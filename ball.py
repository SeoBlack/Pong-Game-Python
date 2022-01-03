from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gray")
        self.penup()
        self.speed("fast")
    def move(self,y,x):
        new_x = self.xcor() + x
        new_y =self.ycor() + y
        self.goto(x=new_x,y=new_y)
    def gameover(self):
        self.goto(0,0)
        self.color("gray")
        self.write("GameOver",False,align="center",font=("Arial", 24, "normal"))










