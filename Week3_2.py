
theFile = open("Week3_2_data.txt", "r")

for aLineOfText in theFile:

    tokens = aLineOfText .split(",")   
    action = tokens[0]
    numberOfSides = tokens[1]
    length = tokens[2]
    print("action = {}, numberOfSides = {}, length={}".format(action, numberOfSides, length))

theFile.close()
