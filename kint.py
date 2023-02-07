import turtle
import winsound
#Game Interface Steup
wn = turtle.Screen()
wn.title("My Ping-Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#scorecounter
sc_a = 0
sc_b = 0
#bat A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("white")
bat_a.shapesize(stretch_wid=5, stretch_len=1)
bat_a.penup()
bat_a.goto(-350, 0)

#bat B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("white")
bat_b.shapesize(stretch_wid=5, stretch_len=1)
bat_b.penup()
bat_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

#ScoreBoard
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0,260)
sb.write("Player A: {}   Player B: {}".format(sc_a,sc_b), align="center", font=("Algerian", 24, "normal"))


#Functions
def bat_a_up():
    y = bat_a.ycor()
    y += 20
    bat_a.sety(y)

def bat_a_down():
    y = bat_a.ycor()
    y -= 20
    bat_a.sety(y)

def bat_b_up():
    y = bat_b.ycor()
    y += 20
    bat_b.sety(y)

def bat_b_down():
    y = bat_b.ycor()
    y -= 20
    bat_b.sety(y)
#Keyboard Binding
wn.listen()
wn.onkeypress(bat_a_up, "w")
wn.onkeypress(bat_a_down, "s")
wn.onkeypress(bat_b_up, "Up")
wn.onkeypress(bat_b_down, "Down")
#Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        sc_a += 1
        sb.clear()
        sb.write("Player A: {}   Player B: {}".format(sc_a,sc_b), align="center", font=("Algerian", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        sc_b += 1
        sb.clear()
        sb.write("Player A: {}   Player B: {}".format(sc_a,sc_b), align="center", font=("Algerian", 24, "normal"))


    #Bat and Ball
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < bat_b.ycor() + 50 and ball.ycor() > bat_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < bat_a.ycor() + 50 and ball.ycor() > bat_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)