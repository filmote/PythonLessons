import turtle

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
theFile = open("Week3_3_data.txt", "r")

for aLineOfText in theFile:

    tokens = aLineOfText .split(",")   
    action = tokens[0]
    numberOfSides = tokens[1]
    length = tokens[2]
    
    print("action = {}, numberOfSides = {}, length={}".format(action, numberOfSides, length))
    polygon(terry, sides = int(numberOfSides), length = int(length))


#Close the file and exit!
theFile.close()
window.exitonclick()