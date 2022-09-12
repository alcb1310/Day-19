from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    tim.rt(10)


def turn_left():
    tim.lt(10)


def clear():
    tim.reset()


screen.listen()
screen.title("Etch-A-Sketch")
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.onkey(key="s", fun=move_backward)
screen.exitonclick()

