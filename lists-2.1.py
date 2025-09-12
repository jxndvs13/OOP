list = []
autodisplay = "n"

while True:
    print ()
    print ("1. Append Element")
    print ("2. Remove Element")
    print ("3. Replace Element")
    print ("4. Sort List")
    print ("5. Reverse List")
    print ("6. Display List")
    print ("7. Toggle Auto Display")
    print ("0. Quit Program")
    print ()
    op = input("Select operation: ")
    print ()

    if op == "1":
        list.append (input ("Add to list: "))
        if autodisplay == "y":
            for p in range(0, len(list)):
                print(list[p])
        elif autodisplay == "n":
            print("operation successful")

    if op == "2":
        print ("1. Input String")
        print ("2. Input Index")
        op2 = input ("Select operation: ")
        if op2 == "1":
            list.remove(input ("Remove from list: "))
        elif op2 == "2":
            index=int(input("Remove from list: "))
            remove=list[index]
            list.remove(remove)
        if autodisplay == "y":
            for p in range(0, len(list)):
                print(list[p])
        elif autodisplay == "n":
            print("operation successful")

    if op == "3":
        index=int(input("Index of Element: "))
        new=input("New Element: ")
        list[index] = new
        if autodisplay == "y":
            for p in range(0, len(list)):
                print(list[p])
        elif autodisplay == "n":
            print("operation successful")

    if op == "4":
        list.sort()
        if autodisplay == "y":
            for p in range(0, len(list)):
                print(list[p])
        elif autodisplay == "n":
            print("operation successful")

    if op == "5":
        list.reverse()
        if autodisplay == "y":
            for p in range(0, len(list)):
                print(list[p])
        elif autodisplay == "n":
            print("operation successful")

    if op == "6":
        for p in range (0, len(list)):
            print (list[p])

    if op == "7":
        if autodisplay == "y":
            autodisplay = "n"
            print ("Auto Display off")
        elif autodisplay == "n":
            autodisplay = "y"
            print ("Auto Display on")

    if op == "0":
        print ("end of operation")
        break