from turtle import Turtle

# Pen
pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Score
score = 0
high_score = 0

def reset_score():
    global score
    # Reset the score
    score = 0
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

def increase_score():
    global score, high_score

    # Increase the score
    score += 10
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))