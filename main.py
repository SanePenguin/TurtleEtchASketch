import turtle as t

screen = t.Screen()
tur = t.Turtle()

screen.listen()
screen.onkey(key="w", fun=lambda:tur.forward(10))
screen.onkey(key="a", fun=lambda:tur.left(10))
screen.onkey(key="s", fun=lambda:tur.forward(-10))
screen.onkey(key="d", fun=lambda:tur.right(10))
screen.onkey(key="c", fun=lambda: screen.clearscreen())

screen.exitonclick()
