from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 265)
        self.color("white")
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"Score: {self.score}\t High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False,align=ALIGNMENT, font=FONT)
