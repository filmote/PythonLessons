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


shapes = ["square", "square", "triangle", "pentagon"] 

for shape in shapes:
    print(shape)

    if shape == "triangle":
        triangle(terry) 

    if shape == "square":
        square(terry) 

    if shape == "pentagon":
        pentagon(terry) 


window.exitonclick()