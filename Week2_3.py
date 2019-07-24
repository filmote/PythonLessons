

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

for x in shapes:

  print("How many sides in a ")
  print(x["name"] )
  print(" ? ")
  print(x["numberOfSides"] )
