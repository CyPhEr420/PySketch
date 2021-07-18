from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


def turn_left():
    turt.left(15)


def turn_right():
    turt.right(15)


def move_backwards():
    turt.back(10)


def clear_screen():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.mainloop()
