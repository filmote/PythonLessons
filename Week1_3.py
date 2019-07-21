import turtle

def triangle(aTurtle):
    for x in range(0, 3):
        aTurtle.right(120)
        aTurtle.forward(100)

def square(aTurtle):
    for x in range(0, 4):
        aTurtle.right(90)
        aTurtle.forward(100)

def pentagon(aTurtle):
    for x in range(0, 5):
        aTurtle.right(72)
        aTurtle.forward(100)


window = turtle.Screen()
window.bgcolor("black")

terry = turtle.Turtle()
terry.shape("turtle")
terry.color("red")


# comments below ..
triangle(terry)
square(terry)
pentagon(terry)

window.exitonclick()