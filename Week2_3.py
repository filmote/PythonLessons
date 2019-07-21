

triangle = {
  "name": "Triangle",
  "numberOfSides": 3
}

square = {
  "name": "Square",
  "numberOfSides": 4
}

pentagon = {
  "name": "Pentagon",
  "numberOfSides": 5
}

shapes = [triangle, square, pentagon]

for shape in shapes:

  print("How many sides in a {0} ? {1}".format(shape["name"] , shape["numberOfSides"] ))
