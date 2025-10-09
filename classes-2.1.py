class Book:
    def __init__(self, nbid, ntitle, nauthor):
        self.bID = nbid
        self.Title = ntitle
        self.Author = nauthor
class User:
    def __init__(self, nuid, nusername):
        self.uID = nuid
        self.username = nusername
        self.borrowed = []
    def display(self):
        print("User ID: ", self.uID)
        print("Username: ", self.username)
        print("Books Borrowed:")
        if len(self.borrowed) >= 1:
            for x in self.borrowed:
                print(x)
        else:
            print("none")
        print("")
    def borrow_s(self,borrowing):
        self.borrowed.append(borrowing)

#maincode
b1 = Book(1,"The Lord of the Rings","J.R.R. Tolkien")
b2 = Book(2,"Percy Jackson & the Olympians","Rick Riordan")
b3 = Book(3,"Harry Potter","J.K. Rowling")
b4 = Book(4,"The Chronicles of Narnia","C.S. Lewis")
b5 = Book(5,"The Adventures of Tom Sayer","Mark Twain")
u1 = User(1,"John Jacob")
u2 = User(2,"Jingleheimer Schmidt")
u1.display()
u2.display()
u1.borrow_s(b1.Title)
u1.borrow_s(b2.Title)
u1.borrow_s(b3.Title)
u2.borrow_s(b4.Title)
u2.borrow_s(b5.Title)
u1.display()
u2.display()
