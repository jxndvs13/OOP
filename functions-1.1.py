def RectArea():
    l = int(input("Input length: "))
    w = int(input("Input width: "))
    print("The area is: ", l*w)

def PrismVol():
    l = int(input("Input length: "))
    w = int(input("Input width: "))
    h = int(input("Input height: "))
    print("The volume is: ", l*w*h)

def CircArea():
    r= int(input("Input radius: "))
    print("The area is: ", 3.14*r*r)

def CylVol():
    r= int(input("Input radius: "))
    print("The volume is: ", 6.28*r)

def SphereVol():
    r= int(input("Input radius: "))
    print("The volume is: ", 4/3*3.14*r*r*r)

#Main Code
while True:
    print ("")
    print ("1. Area of a Rectangle")
    print ("2. Volume of a Rectangular Prism")
    print ("3. Area of a Circle")
    print ("4. Volume of a Cylinder")
    print ("5. Volume of a Sphere")
    print ("0. Quit")
    print ("")
    op = input("Select operation: ")
    print ("")

    if op == "1":
        RectArea()

    elif op == "2":
        PrismVol()

    elif op == "3":
        CircArea()

    elif op == "4":
        CylVol()

    elif op == "5":
        SphereVol()

    elif op == "0":
        break

    else:
        print("Invalid input")