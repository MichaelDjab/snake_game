from turtle import Screen
from snake import Snake
import time
from apple import Apple
from scoreboard import Scoreboard

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE")
scr.tracer(0)

snake = Snake()
apple = Apple()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


end = False
while not end:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # Eat apple
    for segment in snake.segments:
        if segment.distance(apple) < 5:
            apple.refresh()
            scoreboard.increase_score()
            scoreboard.write_score()
            snake.extend()

    # Collide with wall
    x = snake.segments[0].xcor()
    y = snake.segments[0].ycor()
    if x > 280 or x < -290 or y > 290 or y < -280:
        scoreboard.reset()
        snake.reset()

    # Tail collisions
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

scr.exitonclick()

