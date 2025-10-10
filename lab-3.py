class Book:
    def __init__(self):
        self.b_id = ""
        self.title = ""
        self.a_id = ""
        self.publisher = ""
        self.year = ""
class Author:
    def __init__(self):
        self.a_id = ""
        self.name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""
class User:
    def __init__(self):
        self.u_id = ""
        self.username = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.borrowed = []
    def add(self):
        self.u_id = input("User ID: ")
        self.username = input("Username: ")
        makepw = 0
        while makepw == 0:
            npassword = input("Password: ")
            checkpass = input("Check password: ")
            if checkpass == npassword:
                self.password = npassword
                makepw = 1
            else:
                print("Passwords do not match")
                print("Please try again")
                print("")
        self.address = input("Address: ")
        self.phone = input("Phone: ")
        self.email = input("Email: ")
    def display(self):
        print("User ID: ", self.u_id)
        print("Username: ", self.username)
        print("Books Borrowed:")
        if len(self.borrowed) >= 1:
            for x in self.borrowed:
                print(x)
        else:
            print("none")
        print("")
    def check(self):
        print("User ID: ", self.u_id)
        print("Username: ", self.username)
        print("Phone: ", self.phone)
        print("Email: ", self.email)
        print("Books Borrowed:")
        if len(self.borrowed) >= 1:
            for x in self.borrowed:
                print(x)
        else:
            print("none")
    def borrow_s(self,borrowing):
        self.borrowed.append(borrowing)

#maincode
while True:
    print ("")
    print ("1. User Log In")
    print ("2. Create User Account")
    print ("3. Browse Books")
    print ("4. Check Book")
    print ("5. Check Author")
    print ("6. Check User")
    print ("7. Add Book")
    print ("8. Add Author")
    print ("0. Quit")
    print ("")
    op = input("Select Operation: ")

    if op == "1": # User Log In
        print("")
    elif op == "2": # Create User Account
        temp = User()
        User.add(temp)
    elif op == "3": # Browse Books
        print("")
    elif op == "4": # Check Book
        print("")
    elif op == "5": # Check Author
        print("")
    elif op == "6": # Check User
        ch_u=input("Enter User ID: ")
        User.check(ch_u)
    elif op == "7": # Add Book
        print("")
    elif op == "8": # Add Author
        print("")
    elif op == "0":
        print ("End Program")
        break
    else:
        print ("Invalid Operation")