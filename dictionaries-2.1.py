Projects = {"p1":{
                    
}}

while True:
    print ("")
    print ("1. Project Initiation")
    print ("2. Project Closure")
    print ("3. Project Progress Update")
    print ("4. Print Project Info")
    print ("5. Print all Info")
    print ("0. Quit")
    op = input("Select Operation: ")
    print ("")

    if op == "1": #Project Initiation
        nID = input("Enter Project ID: ")
        nTitle = input("Enter Project Title: ")
        nManager = input("Add 1 Project Manager: ")
        nStart = input("Enter Start Date: ")
        nEnd = input("Enter End Date: ")
        nSponsor = input("Enter Sponsor Name: ")
        nBudget = input("Enter Budget: ")
        nTechnology = input("Add 1 Technology: ")
        nTeam = input("Add 1 Team Member: ")
        Projects[nID] = {"title":nTitle,
                         "managers":[nManager],
                         "start":nStart,
                         "end":nEnd,
                         "sponsor":nSponsor,
                         "budget":nBudget,
                         "technologies":[nTechnology],
                         "team":[nTeam]}
        print ("")
        print ("Project Initiated")
        edit = 1
        while edit == 1:
            print ("")
            print ("Add Additional Elements?")
            print ("1. Add Project Manager")
            print ("2. Add Technology")
            print ("3. Add Team Member")
            print ("0. Finish Initialization")
            nop = input("Select Operation: ")
            print ("")
            if nop == "1":
                nManager = input("Enter Project Manager: ")
                Projects[nID]["managers"].append(nManager)
                print(nManager, "added to", nTitle)
            elif nop == "2":
                nTechnology = input("Enter Technology: ")
                Projects[nID]["technologies"].append(nTechnology)
                print(nTechnology, "added to", nTitle)
            elif nop == "3":
                nTeam = input("Enter Team Member: ")
                Projects[nID]["team"].append(nTeam)
                print(nTeam, "added to", nTitle)
            elif nop == "0":
                print ("Initiation Complete")
                edit = 0
            else:
                print("Invalid Operation")

    elif op == "2": #Project Closure
        dID = input("Enter Project ID: ")
        dTitle = Projects[dID]["title"]
        print("Are you sure you want to close", dTitle, "(y/n)? (this project will be deleted forever)")
        dYN = input()
        if dYN == "y":
            del Projects[dID]
            print ("Project Closed")
        if dYN == "n":
            print ("operation cancelled")

    elif op == "3": #Project Update
        eID = input("Enter Project ID: ")
        edit = 1
        while edit == 1:
            print ("")
            print (Projects[eID])
            print ("")
            print ("1. Update Project Managers")
            print ("2. Update End Date")
            print ("3. Update Sponsor")
            print ("4. Update Budget")
            print ("5. Update Technologies")
            print ("6. Update Team Members")
            print ("0. End Edit Session")
            eop = input("Select Operation: ")
            if eop == "1":
                print ("1. Add Project Manager")
                print ("2. Remove Project Manager")
                print ("0. Back")
                mop = input("Select Operation: ")
                if mop == "1":
                    nManager = input("Enter Project Manager: ")
                    Projects[eID]["managers"].append(nManager)
                    print(nManager, "added to project")
                if mop == "2":
                    dManager = input("Enter Project Manager: ")
                    Projects[eID]["managers"].delete(dManager)