from turtle import Turtle
segments = []

class Snake:

    def __init__(self):
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in initial_positions:
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("#7c9473")
            snake_segment.goto(pos)
            segments.append(snake_segment)

    def move(self):
        for seg in range((len(segments) - 1), 0, -1):
            new_x = segments[seg - 1].xcor()
            new_y = segments[seg - 1].ycor()
            segments[seg].goto(new_x, new_y)
        segments[0].forward(20)

