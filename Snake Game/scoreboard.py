from turtle import Screen, Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

with open("high_score.txt", mode="r") as file:
    high_score = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        print("hello")
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.highscore = int(high_score)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Total Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        with open("high_score.txt", mode="w") as file2:
            file2.write(str(self.highscore))
            print("hello")
        self.score = 0
        self.clear()
        self.update_scoreboard()

        
    
