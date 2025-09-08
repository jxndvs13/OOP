list = []

while True:
    print ()
    print ("1. Append to the list")
    print ("2. Remove from the list")
    print ("3. Pop an element from the list")
    print ("4. Display the list")
    print ("0. Quit")
    print ()
    op = input("Select operation: ")
    print ()

    if op == "1":
        list.append (input ("Add to list:"))
        print ("operation successful")

    if op == "2":
        list.remove (input ("Remove from list:"))
        print ("operation successful")

    if op == "3":
        list.pop()
        print ("operation successful")

    if op == "4":
        for p in range (0, len(list)):
            print (list[p])

    if op == "0":
        print ("end of operation")
        break