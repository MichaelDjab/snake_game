from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 265)
        self.color("white")
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False,align=ALIGNMENT, font=FONT)
