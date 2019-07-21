import turtle

def polygon(aTurtle, sides, length):

    angle = 360 / sides

    for x in range(0, sides):
        aTurtle.right(angle)
        aTurtle.forward(length)


window = turtle.Screen()
window.bgcolor("black")

terry = turtle.Turtle()
terry.shape("turtle")
terry.color("red")

# comments below ..
polygon(terry, 3, 100)
polygon(terry, 4, 100)
polygon(terry, 5, 100)

window.exitonclick()