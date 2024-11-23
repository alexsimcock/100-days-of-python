import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a colour: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_racers = [Turtle(shape="turtle") for _ in colors]

for index, turtle in enumerate(turtle_racers):
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=-160 + 64 * index)

if user_bet:
    is_race_on = True

# We shuffle turtles before racing to avoid red (index 0) turtle always having the first move.
random.shuffle(turtle_racers)

while is_race_on:
    for turtle in turtle_racers:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
