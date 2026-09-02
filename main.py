from turtle import Turtle
from main_functions import move, screen, head, reset_game, segments
from score import pen, reset_score, increase_score
from snake_food import food, eat_food, making_tail
import time


delay = 0.1

# Main Game Logic

while True:
    screen.update()

    # Collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # Eating the food
    if head.distance(food) < 20:
        eat_food()
        increase_score()

    making_tail()

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(delay)

screen.mainloop()