queue = []

def Enqueue():
    new = input ("Add to Queue: ")
    queue.append(new)

def Dequeue():
    if len(queue) != 0:
        rid = queue[0]
        queue.remove(rid)
    else:
        print ("Queue is empty")

def Display():
    if len(queue) == 0:
        print ("Queue is empty")
    else:
        print (queue)

while True:
    print ("")
    print ("1. Add to Queue")
    print ("2. Remove from Queue")
    print ("3. Display Queue")
    print ("4. Toggle Autodisplay")
    print ("0. Quit")
    print ("")
    op = input("Select operation: ")
    print ("")

    if op == "1":
        Enqueue()

    elif op == "2":
        Dequeue()

    elif op == "3":
        Display()

    elif op == "4":
        Autodisplay()

    elif op == "0":
        break

    else:
        print("Invalid input")