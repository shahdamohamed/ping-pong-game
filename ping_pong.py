import turtle

# screen setting
wind = turtle.Screen()
wind.title("PING PONG BY ***SHAHDA***")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()
madrab1.goto(-350, 0)
madrab1.shapesize(stretch_wid=5, stretch_len=1)

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# score variables
score1 = 0
score2 = 0

# score display
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# functions for moving the paddles
def madrab1_up():
    y = madrab1.ycor()
    if y < 250:  
        y += 20
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    if y > -240:  
        y -= 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    if y < 250:  
        y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    if y > -240:  
        y -= 20
    madrab2.sety(y)

# keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# main game loop
while True:
    wind.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border collision (top and bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # goal scoring (left and right)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))

    # paddle collision with ball
    if (340 < ball.xcor() < 350) and (madrab2.ycor() - 50 < ball.ycor() < madrab2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (madrab1.ycor() - 50 < ball.ycor() < madrab1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
