from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in INITIAL_POSITIONS:
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("#7c9473")
            snake_segment.goto(pos)
            self.segments.append(snake_segment)

    def move(self):
        for seg in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

