import turtle

def drawSegment(aTurtle, length):

  aTurtle.right(20)
  aTurtle.forward(length)

  if length < 150:
    drawSegment(aTurtle, length + 1)


# -------------------------------------------------

window = turtle.Screen()
window.bgcolor("black")

terry = turtle.Turtle()
terry.shape("turtle")
terry.color("red")

drawSegment(terry, 5)

window.exitonclick()