from turtle import Screen
from snake import Snake
import time
from apple import Apple

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE")
scr.tracer(0)

snake = Snake()
apple = Apple()

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


scr.exitonclick()

