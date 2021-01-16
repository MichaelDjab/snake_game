from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in INITIAL_POSITIONS:
            self.add_segment(pos)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def add_segment(self, pos):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("#7c9473")
        snake_segment.goto(pos)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if not self.segments[0].heading() == DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if not self.segments[0].heading() == UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if not self.segments[0].heading() == RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if not self.segments[0].heading() == LEFT:
            self.segments[0].setheading(RIGHT)

