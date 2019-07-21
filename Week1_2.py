import turtle

def polygon(aTurtle, sides, length):

    counter = 0
    angle = 360 / sides

    while counter < sides:
        aTurtle.right(angle)
        aTurtle.forward(length)
        counter = counter + 1


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