#Define a class: Book (BookID, BookName, Title, Author)
#Define a class User (userID, userName, Booksborrowed=[]
#create 5 book objects
#create 2 user objects
#add books to the users

class Book:
    def __init__(self, nbID, nTitle, nAuthor):
        self.bID = ""
        self.Title = ""
        self.Author = ""
        self.copies = ""
class User:
    def __init__(self):
        self.uID = ""
        self.username = ""
        self.borrowed = []

#maincode
b1 = Book()