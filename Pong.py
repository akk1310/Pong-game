from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time







screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))



ball=Ball()
scoreboard=Scoreboard()
button = Turtle()
button.hideturtle()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

def create_button():
    button = Turtle()
    button.hideturtle()
    button.penup()
    button.goto(0, -100)
    button.color("white")
    button.write("Restart", align="center", font=("Courier", 24, "normal"))
    button.shape("square")
    button.shapesize(stretch_wid=2, stretch_len=5)
    button.showturtle()
    return button

def on_click(x, y):
    if -50 < x < 50 and -120 < y < -80:
        button.clear()
        button.hideturtle()
        game()





def game():
    global game_is_on
    game_is_on=True
    scoreboard.reset()
    ball.reset_position()
    l_paddle.goto(-350, 0)
    r_paddle.goto(350, 0)
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        #Detect collision with ball
        if ball.ycor()>280 or ball.ycor()<-280 :
            ball.bounce_y()
        #Detect collision with paddle
        if (ball.xcor()>320 and ball.distance(r_paddle)<50) or (ball.xcor()<-320 and ball.distance(l_paddle)<50):
            ball.bounce_x()
            
        #detect if ball goes out of bound
        #right
        if ball.xcor()>380: 
            ball.reset_position()
            scoreboard.l_point()

        #left
        if ball.xcor()<-380:
            ball.reset_position()
            scoreboard.r_point()
        def game():
            game_is_on=False
        
        if scoreboard.l_score > 1 or scoreboard.r_score >1 :
            game_is_on=False
            scoreboard.game_over()
            global button
            button = create_button()
            screen.onscreenclick(on_click)

        

game()


# screen.onkey(game, "Return")


screen.mainloop()

