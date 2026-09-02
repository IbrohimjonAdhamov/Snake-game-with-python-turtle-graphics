from turtle import Turtle
from main_functions import segments, head
import random


# Snake Food
food = Turtle()
food.shape("circle")
food.speed(0)
food.penup()
food.color("red")
food.goto(100, 100)

def eat_food():
    # move the food to a random spot
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

    # Add a segment
    new_segment = Turtle()
    new_segment.speed(0)
    new_segment.color("orange")
    new_segment.shape("square")
    new_segment.penup()
    segments.append(new_segment)

def making_tail():
    # Move the end segments == following as one tail
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
