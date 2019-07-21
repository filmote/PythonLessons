import turtle

def polygon(aTurtle, sides, length):

    counter = 0
    angle = 360 / sides

    while counter < sides:
        aTurtle.right(angle)
        aTurtle.forward(length)
        counter = counter + 1

# -------------------------------------------------
# set up our shapes
#
triangle = {
  "name": "Triangle",
  "numberOfSides": 3,
  "length": 120
}

small_square = {
  "name": "Square",
  "numberOfSides": 4,
  "length": 70
}

big_square = {
  "name": "Square",
  "numberOfSides": 4,
  "length": 150
}

pentagon = {
  "name": "Pentagon",
  "numberOfSides": 5,
  "length": 60
}

shapes = [triangle, small_square, big_square, pentagon]


# -------------------------------------------------
# draw our shapes
#
window = turtle.Screen()
window.bgcolor("black")

terry = turtle.Turtle()
terry.shape("turtle")
terry.color("red")

for shape in shapes:

  polygon(terry, sides = shape["numberOfSides"], length = shape["length"])


window.exitonclick()