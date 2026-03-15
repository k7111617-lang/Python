import turtle
turtle.Screen().bgcolor("orange")
polygon=turtle.Turtle()
sides=6
angle=360/sides
side_length=85
for i in range(sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()