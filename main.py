from turtle import Turtle, Screen
import time
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE")
scr.tracer(0)

initial_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for pos in initial_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.penup()
    snake_segment.color("#7c9473")
    snake_segment.goto(pos)
    segments.append(snake_segment)
    scr.update()

end = False

while not end:
    scr.update()
    time.sleep(0.1)
    for seg in range((len(segments) - 1), 0, -1):
        new_x = segments[seg-1].xcor()
        new_y = segments[seg-1].ycor()
        segments[seg].goto(new_x, new_y)
        segments[seg].color("red")
        scr.update()
        segments[seg].color("#7c9473")
        time.sleep(0.1)
    segments[0].forward(20)
    segments[0].right(90)






scr.exitonclick()
