from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forwards():
    """Moves turtle forward by 10.
    """
    tim.forward(10)

def move_backwards():
    """Moves turtle backward by 10.
    """
    tim.backward(10)

def move_cclockwise():
    """Moves turtle counter-clockwise.
    """
    tim.left(10)

def move_clockwise():
    """Moves turtle clockwise.
    """
    tim.right(10)

def clear_drawing():
    """Clears turtle GUI and resets turtle.
    """
    tim.reset()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_cclockwise)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkeypress(key="c", fun=clear_drawing)

screen.exitonclick()
