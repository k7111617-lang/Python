import turtle
turtle.Screen().bgcolor("green")
board=turtle.Turtle()
for i in range(140):
    board.forward(i*5)
    board.right(90)
turtle.done()