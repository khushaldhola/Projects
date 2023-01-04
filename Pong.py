import turtle
import winsound # for sound we need in windows "os" is for linux/mac

wn = turtle.Screen()
wn.title("Pong by Khushal4o4")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stop window from updating, sowe have to manually updating #it speed ups our game quite a bit
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()  # turtle objact t->module name, T->class name
# speed of animation, set to mamimum possible speed otherwise it is very slow
paddle_a.speed(0)
paddle_a.shape("square")  # 20px * 20px
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # make it 100 tal
paddle_a.penup()  # draw a line
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# x movements
ball.dx = 0.1  # delta change, every time ball s move is moved by 2px
# y movements
ball.dy = 0.1  # here if we put -0.1 it goes from down side

# Scoring System

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
# shape doesnt matter beacause we cant see it
pen.penup()  # beacause we dont wanna line when pen move
pen.hideturtle()  # we dont wanna see so we hide it
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center",
          font=("Courier", 24, "normal"))  # default score


# Functions


def paddle_a_up():
    y = paddle_a.ycor()  # gives cordinates of y axis
    y += 20  # add 20 px to the y cordinates
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # gives cordinates of y axis
    y -= 20  # add 20 px to the y cordinates
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # gives cordinates of y axis
    y += 20  # add 20 px to the y cordinates
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # gives cordinates of y axis
    y -= 20  # add 20 px to the y cordinates
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # tells us to listen for keyboard input
# when the user press lower "w" call the fun paddle_a_up
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")  # for up arrow
wn.onkeypress(paddle_b_down, "Down")  # for down arrow


# Main game
while True:
    wn.update()  # every time loop runs the screen is updated

    # move the ball
    ball.setx(ball.xcor() + ball. dx)
    ball.sety(ball.ycor() + ball. dy)

    # Border cheking ,cause our ball is going out of the 600 height
    if ball.ycor() > 290:          # 600 - 20 / 2 = 290
        ball.sety(290)             # set back to 290
        ball.dy *= -1              # reverces the diration
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # every thing is stopped when this sound play so we need to add " winsound.SND_ASYNC "
        #os.system(afplay bounce.wav&) # sound play for mac
        #every thing is stopped when this sound play so we need to add & at the end

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:          # 800 - 20 / 2 = 390 & - 40 for aligning it depends on you
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball collition
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
