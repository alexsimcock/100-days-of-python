import time
from turtle import Screen, Turtle


class SnakeSegment(Turtle):
    def __init__(self, prior_segment=None):
        super().__init__()
        self.prior_segment = prior_segment
        self.shape("square")
        self.color("white")
        self.penup()

    def update_position(self):
        if self.prior_segment:
            self.goto(self.prior_segment.position())


class Snake:
    def __init__(self, start_length=3):
        self.head = SnakeSegment()
        self.segments = [self.head]

        for _ in range(start_length):
            self.segments.append(SnakeSegment(prior_segment=self.segments[-1]))

        starting_positions = [(i * -20, 0) for i in range(start_length)]
        for segment, position in zip(self.segments, starting_positions):
            segment.goto(position)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake(start_length=3)
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake.segments[1:]:
        segment.goto(segment.prior_segment.position())
    snake.segments[0].forward(20)

screen.exitonclick()
