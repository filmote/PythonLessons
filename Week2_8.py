dict = {}

while (True):

    print(" ")
    print("- Add a new Entry -----------------------------------------")
    print(" ")

    x = input("New Name: ")

    if x.lower() == 'exit':
        break
        
    y = input("New Age: ")

    dict[x] = y

    print(" ")
    print("- Current List --------------------------------------------")
    print(" ")

    for a in dict:

        print("Name: {}, ".format(a), end="" )
        print("Age: {}".format( dict[a] ) )
