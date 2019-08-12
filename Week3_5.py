import turtle
import xml.etree.ElementTree as ET

def polygon(aTurtle, sides, length):

    counter = 0
    angle = 360 / sides

    while counter < sides:
        aTurtle.right(angle)
        aTurtle.forward(length)
        counter = counter + 1


# -------------------------------------------------
# draw our shapes
#
window = turtle.Screen()
window.bgcolor("black")

terry = turtle.Turtle()
terry.shape("turtle")
terry.color("red")


# Read from the file ..
xmlDocument = ET.parse('Week3_5_data.xml')
actions = xmlDocument.getroot()

for action in actions:

    numberOfSides = action.get('numberOfSides')
    length = action.get('length')

    print("numberOfSides = {}, length = {}".format(numberOfSides, length))
    polygon(terry, sides = int(numberOfSides), length = int(length))


window.exitonclick()