dict = {}

while (True):

    print(" ")
    print("- Add a new Entry -----------------------------------------")
    print(" ")

    key = input("New Name: ")
    val = input("New Age: ")

    dict[key] = val

    print(" ")
    print("- Current List --------------------------------------------")
    print(" ")

    for key in dict:

        print("Name: ", end="" )
        print(key, end="" )
        print(", Age: ", end="" )
        print( dict[key] ) 

#        print("Name: {}, ".format(key), end="" )
#        print("Age: {}".format( dict[key] ) )
