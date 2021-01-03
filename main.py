from turtle import Screen
from snake import Snake
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE")
scr.tracer(0)

snake = Snake()

end = False
while not end:
    scr.update()
    time.sleep(0.1)
    snake.move()


scr.exitonclick()
