dict = {}

theFile = open("Week3_6_data.txt", "r")


print(" ")
print("- Read File --------------------------------------------")
print(" ")

for aLineOfText in theFile:

    parts = aLineOfText .split(",")   
    name = parts[0]
    age = parts[1]
    print("name = {}, age = {}".format(name, age))

    dict[name] = age

print(" ")
print("- The List --------------------------------------------")
print(" ")

for key in dict:

    print("Name: ", end="" )
    print(key, end="" )
    print(", Age: ", end="" )
    print( dict[key] ) 


theFile.close()
