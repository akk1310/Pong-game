from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("courier",60,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("courier",60,"normal"))

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.color("red")
            
        if self.l_score>self.r_score:
            self.write(f"Left Wins by {self.l_score-self.r_score}",align="center",font=("courier",60,"normal"))
        elif self.l_score<self.r_score:
            self.write(f"Right Wins by {self.r_score-self.l_score}",align="center",font=("courier",60,"normal"))
        else:
            self.write(f"Tie",align="center",font=("courier",60,"normal"))
        self.color("blue")
        

    def reset(self):
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()