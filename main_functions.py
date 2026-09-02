from turtle import Turtle, Screen
import time
from score import reset_score

segments = []


# Snake attributes
head = Turtle()
head.shape("square")
head.speed(0)
head.penup()
head.color("black")
head.goto(0, 0)
head.direction = "stop"


# Screen attributes
screen = Screen()
screen.bgcolor("green")
screen.title("Snake Game by ibrohimjonreal")
screen.setup(width=600, height=600)
screen.tracer(0)

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx (x + 20)


def reset_game():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments == cutting the tail
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()
    reset_score()


#Keyboard Bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
