from turtle import Turtle
class ScoreBoard(Turtle):#creating the scoreboard that will count for each player
    def __init__(self):
        super().__init__()
        self.color("gray")
        self.player1 = 0
        self.player2 = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()



    def update_scoreboard(self):#updating the scoreboard after each point
        self.clear()
        self.goto(100, 260)
        self.write(self.player2,move=False,align="center",font=("Arial",24,"normal"))
        self.goto(-100,260)
        self.write(self.player1, move=False, align="center", font=("Arial", 24, "normal"))
    def increase_score_player_1(self):#left player
        self.player1 += 1
    def increase_score_player_2(self):#right player
        self.player2 += 1
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAMEOVER", move=False, align="center", font=("Arial", 24, "normal"))

