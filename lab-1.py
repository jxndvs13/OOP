while True:
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("0. Quit")
    op = input ("Select an operation: ")

    if op == "1":
        print (" ")
        n1 = int(input ("1st number: "))
        n2 = int(input ("2nd number: "))
        print (n1, "+", n2, "=", n1 + n2)
        print (" ")
    elif op == "2":
        print (" ")
        n1 = int(input ("1st number: "))
        n2 = int(input ("2nd number: "))
        print (n1, "-", n2, "=", n1 - n2)
        print (" ")
    elif op == "3":
        print (" ")
        n1 = int(input ("1st number: "))
        n2 = int(input ("2nd number: "))
        print (n1, "*", n2, "=", n1 * n2)
        print (" ")
    elif op == "4":
        print (" ")
        n1 = int(input ("1st number: "))
        n2 = int(input ("2nd number: "))
        print (n1, "/", n2, "=", n1 / n2)
        print (" ")
    elif op == "0":
        break