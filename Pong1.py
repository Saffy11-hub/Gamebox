import turtle
import winsound

wdow = turtle.Screen()
wdow.title("Pong by @ChefSaffy")
wdow.bgcolor("black")
wdow.setup(width=800, height=600)
wdow.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def pad_a_up():
     y = pad_a.ycor()
     y += 20
     pad_a.sety(y)

def pad_a_down():
     y = pad_a.ycor()
     y -= 20
     pad_a.sety(y)

def pad_b_up():
     y = pad_b.ycor()
     y += 20
     pad_b.sety(y)

def pad_b_down():
     y = pad_b.ycor()
     y -= 20
     pad_b.sety(y)

# Keyboard binding
wdow.listen()
wdow.onkeypress(pad_a_up, "q")
wdow.onkeypress(pad_a_down, "a")
wdow.onkeypress(pad_b_up, "Up")
wdow.onkeypress(pad_b_down, "Down")

# Main game loop
while True:
     wdow.update() 

     # Move the ball
     ball.setx(ball.xcor() + ball.dx)
     ball.sety(ball.ycor() + ball.dy)

     # Border checking
     if ball.ycor() > 290:
          ball.sety(290)
          ball.dy *= -1
          winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

     if ball.ycor() < -290:
          ball.sety(-290)
          ball.dy *= -1
          winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

     if ball.xcor() > 390:
          ball.goto(0, 0)
          ball.dx *= -1
          score_a += 1
          pen.clear()
          pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


     if ball.xcor() < -390:
          ball.goto(0, 0)
          ball.dx *= -1
          score_b += 1
          pen.clear()
          pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


     # Paddle and Ball collisions
     if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() -40):
          ball.setx(340)
          ball.dx *= -1
          winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

     if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
          ball.setx(-340)
          ball.dx *= -1
          winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)





