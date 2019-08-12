
theFile = open("Week3_2_data.txt", "r")

for aLineOfText in theFile:

    parts = aLineOfText .split(",")   
    action = parts[0]
    numberOfSides = parts[1]
    length = parts[2]
    print("action = {}, numberOfSides = {}, length={}".format(action, numberOfSides, length))

theFile.close()
