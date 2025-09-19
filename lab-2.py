myStudents = {"Jaxon":{
                    "lab-1":10,
                    "lab-2":8,
                    "lab-3":9,
                    "lab-4":10,
                    "lab-5":6
                    }}
myStudents["Jaxon"]["total"] = myStudents["Jaxon"]["lab-1"] + myStudents["Jaxon"]["lab-2"] + myStudents["Jaxon"]["lab-3"] + myStudents["Jaxon"]["lab-4"] + myStudents["Jaxon"]["lab-5"]
myStudents["Jaxon"]["percent"] = myStudents["Jaxon"]["total"] * 2
myStudents["Jaxon"]["average"] = myStudents["Jaxon"]["total"] / 5
while True:
    print ("")
    print ("1. Add a Student")
    print ("2. Delete a Student")
    print ("3. Modify a Student")
    print ("4. Display one Student")
    print ("5. Display all Students")
    print ("0. Quit")
    op = input("Select operation: ")
    print ("")

    if op == "1": # Add Student
        nname = input("Enter new student name: ")
        nlab1 = int(input("Enter lab 1 grade: "))
        nlab2 = int(input("Enter lab 2 grade: "))
        nlab3 = int(input("Enter lab 3 grade: "))
        nlab4 = int(input("Enter lab 4 grade: "))
        nlab5 = int(input("Enter lab 5 grade: "))
        myStudents.update ({nname:{"lab-1":nlab1, "lab-2":nlab2, "lab-3":nlab3, "lab-4":nlab4, "lab-5":nlab5}})
        myStudents[nname]["total"] = myStudents[nname]["lab-1"] + myStudents[nname]["lab-2"] + myStudents[nname]["lab-3"] + myStudents[nname]["lab-4"] + myStudents[nname]["lab-5"]
        myStudents[nname]["percent"] = myStudents[nname]["total"] * 2
        myStudents[nname]["average"] = myStudents[nname]["total"] / 5
        print (nname, "added successfully")

    elif op == "2":  # Delete Student
        dname = input("Enter student name: ")
        ays = input("Are you sure? (y/n): ")
        if ays == "y":
            del myStudents[dname]
            print("student deleted")
        if ays == "n":
            print("operation cancelled")

    elif op == "3": # Edit Student
        ename = input("Enter student name: ")
        editing = 1
        while editing == 1:
            myStudents[ename]["total"] = myStudents[ename]["lab-1"] + myStudents[ename]["lab-2"] + myStudents[ename]["lab-3"] + myStudents[ename]["lab-4"] + myStudents[ename]["lab-5"]
            myStudents[ename]["percent"] = myStudents[ename]["total"] * 2
            myStudents[ename]["average"] = myStudents[ename]["total"] / 5
            print("Lab-1:", myStudents[ename]["lab-1"])
            print("Lab-2:", myStudents[ename]["lab-2"])
            print("Lab-3:", myStudents[ename]["lab-3"])
            print("Lab-4:", myStudents[ename]["lab-4"])
            print("Lab-5:", myStudents[ename]["lab-5"])
            print("0. Quit")
            elab = input("Select lab to edit or other operation: ")
            if elab == "1":
                elab1 = int(input("Updated grade: "))
                myStudents[ename]["lab-1"] = elab1
                print ("Lab-1 grade updated to", elab1)
                print ("")
            elif elab == "2":
                elab2 = int(input("Updated grade: "))
                myStudents[ename]["lab-2"] = elab2
                print ("Lab-2 grade updated to", elab2)
                print ("")
            elif elab == "3":
                elab3 = int(input("Updated grade: "))
                myStudents[ename]["lab-3"] = elab3
                print ("Lab-3 grade updated to", elab3)
                print ("")
            elif elab == "4":
                elab4 = int(input("Updated grade: "))
                myStudents[ename]["lab-4"] = elab4
                print ("Lab-4 grade updated to", elab4)
                print ("")
            elif elab == "5":
                elab5 = int(input("Updated grade: "))
                myStudents[ename]["lab-5"] = elab5
                print ("Lab-5 grade updated to", elab5)
                print ("")
            elif elab == "0":
                print ("editing session ended")
                break
            else:
                print("invalid operation")

    elif op == "4": # Display one student
        dname = input("Enter student name: ")
        print (myStudents[dname])

    elif op == "5": # Display all students
        for n in myStudents.items():
            print (n)

    elif op == "0":
        print ("end of line")
        break