from turtle import Turtle, Screen

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE")




head = Turtle(shape="square")
head.penup()
head.color("#295939")

body1 = Turtle(shape="square")
body1.penup()
body1.color("#7c9473")
body1.goto(-20, 0)

tail = Turtle(shape="square")
tail.penup()
tail.color("#cfdac8")
tail.goto(-40, 0)










scr.exitonclick()
