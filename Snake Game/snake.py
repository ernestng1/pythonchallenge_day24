from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)
            
    def add_segment(self, position):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.snake_length.append(turtle)
    
    def extend(self):
        self.add_segment(self.snake_length[-1].position())

    def reset(self):
        for i in self.snake_length:
            i.goto(1000,1000)
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]
        
    def move(self):
        for i in range(len(self.snake_length)-1,0,-1):
            new_x = self.snake_length[i-1].xcor()
            new_y = self.snake_length[i-1].ycor()
            self.snake_length[i].goto(new_x, new_y)
        self.snake_length[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
