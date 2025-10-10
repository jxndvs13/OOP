class Book:
    def __init__(self, new_id):
        self.b_id = new_id
        self.title = ""
        self.a_id = ""
        self.publisher = ""
        self.year = ""
    def add(self):
        print("Create Book with ID: ", self.b_id)
        self.title = input("Title: ")
        self.a_id = input("Author ID: ")
        self.publisher = input("Publisher: ")
        self.year = input("Publication Year: ")
    def display(self, b_auth):
        print("Book ID: ", self.b_id)
        print("Title: ", self.title)
        print("Author: ", b_auth)
        print("Publisher: ", self.publisher)
        print("Publication Year: ", self.year)
class Author:
    def __init__(self, new_id):
        self.a_id = new_id
        self.name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""
    def add(self):
        print("Create Author with ID: ", self.a_id)
        self.name = input("Name: ")
        self.affiliation = input("Affiliation: ")
        self.country = input("Country: ")
        self.phone = input("Phone: ")
        self.email = input("Email: ")
    def display(self):
        print("Author ID: ", self.a_id)
        print("Name: ", self.name)
        print("Affiliation: ", self.affiliation)
        print("Home Country: ", self.country)
        print("Phone Number: ", self.phone)
        print("Email Address: ", self.email)
class User:
    def __init__(self, new_id):
        self.u_id = new_id
        self.username = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.borrowed = []
    def add(self):
        print("Create Account for User: ", self.u_id)
        self.username = input("Username: ")
        makepw = 0
        while makepw == 0:
            n_pass = input("Password: ")
            checkpass = input("Check Password: ")
            if checkpass == n_pass:
                self.password = n_pass
                makepw = 1
            else:
                print("Passwords do not match")
                print("Please try again")
                print("")
        self.address = input("Address: ")
        self.phone = input("Phone Number: ")
        self.email = input("Email: ")
    def display(self):
        print("User ID: ", self.u_id)
        print("Username: ", self.username)
        print("Address: ", self.address)
        print("Phone Number: ", self.phone)
        print("Email Address: ", self.email)
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
        print("Phone Number: ", self.phone)
        print("Email Address: ", self.email)
        print("Books Borrowed:")
        if len(self.borrowed) >= 1:
            for x in self.borrowed:
                print(x)
        else:
            print("none")
    def borrow(self,borrowing):
        self.borrowed.append(borrowing)
    def login(self):
        password = input(f"Enter Password for {self.u_id}: ")
        if password == self.password:
            print("Login Successful")
            return 1
        else:
            print("Incorrect Password")
            return 0
    def update(self):
        User.display(self)
        print("Update Account for User: ", self.u_id)
        self.username = input("New Username: ")
        makepw = 0
        while makepw == 0:
            n_pass = input("New Password: ")
            checkpass = input("Check Password: ")
            if checkpass == n_pass:
                self.password = n_pass
                makepw = 1
            else:
                print("Passwords do not match")
                print("Please try again")
                print("")
        self.address = input("New Address: ")
        self.phone = input("New Phone Number: ")
        self.email = input("New Email: ")
        User.display(self)
def f_author_id(id_find, authors_all):
    for find_a in authors_all:
        if find_a.a_id == id_find:
            return find_a
    return None
def f_author_name(name_find, authors_all):
    for find_a in authors_all:
        if find_a.name == name_find:
            return find_a
    return None
def f_book_id(id_find, books_all):
    for find_b in books_all:
        if find_b.b_id == id_find:
            return find_b
    return None
def f_book_title(title_find, books_all):
    for find_b in books_all:
        if find_b.title == title_find:
            return find_b
    return None
def f_user_id(id_find, users_all):
    for find_u in users_all:
        if find_u.u_id == id_find:
            return find_u
    return None
def f_user_name(name_find, users_all):
    for find_u in users_all:
        if find_u.username == name_find:
            return find_u
    return None
def f_user_ad(ad_find, users_all):
    for find_u in users_all:
        if find_u.address == ad_find:
            return find_u
    return None
book_counter = 1
user_counter = 1
auth_counter = 1
logged_in = 0
all_books = []
all_users = []
all_authors = []
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

    # User Log In
    if op == "1":
        uid = input("Enter User ID: ")
        logged_user = f_user_id(uid, all_users)
        if logged_user:
            logged_in = User.login(logged_user)
            while logged_in == 1:
                print("")
                print("1. Display User Account")
                print("2. Browse Books")
                print("3. Check Book")
                print("4. Check Author")
                print("5. Update User Account")
                print("0. Log Out")
                print("")
                uop = input("Select Operation")
                if uop == "1": # Display
                    print("")
                if uop == "2": # Browse
                    print("")
                if uop == "3": # Book
                    print("1. ID")
                    print("2. Title")
                    print("0. Back")
                    method = input("Choose Search Method: ")
                    print("")
                    if method == "1":
                        find_id = input("Enter Book ID: ")
                        found_b = f_book_id(find_id, all_books)
                        if found_b:
                            author = found_b.a_id
                            a_name = f_author_id(author, all_authors)
                            Book.display(found_b, a_name)
                            q_borrow = input("Borrow Book? (Y/N)")
                            if q_borrow == "Y" or q_borrow == "y":
                                found_title = found_b.title
                                User.borrow(logged_user, found_title)
                            elif q_borrow == "N" or q_borrow == "n":
                                print("Book not Borrowed")
                            else:
                                print("Book not Borrowed (invalid input)")
                        else:
                            print("Book not found")
                    elif method == "2":
                        find_title = input("Enter Book Title: ")
                        found_b = f_book_title(find_title, all_books)
                        if found_b:
                            author = found_b.a_id
                            a_name = f_author_id(author, all_authors)
                            Book.display(found_b, a_name)
                            q_borrow = input("Borrow Book? (Y/N)")
                            if q_borrow == "Y" or q_borrow == "y":
                                found_title = found_b.title
                                User.borrow(logged_user, found_title)
                            elif q_borrow == "N" or q_borrow == "n":
                                print("Book not Borrowed")
                            else:
                                print("Book not Borrowed (invalid input)")
                        else:
                            print("Book not found")
                    elif method == "0":
                        print("Search Canceled")
                    else:
                        print("Invalid Operation")
                if uop == "4": # Author
                    print("1. ID")
                    print("2. Name")
                    print("0. Back")
                    method = input("Choose Search Method: ")
                    print("")
                    if method == "1":
                        find_id = input("Enter Author ID: ")
                        found_a = f_author_id(find_id, all_authors)
                        if found_a:
                            Author.display(found_a)
                        else:
                            print("Author not found")
                    elif method == "2":
                        find_title = input("Enter Author Name: ")
                        found_a = f_author_name(find_title, all_authors)
                        if found_a:
                            Author.display(found_a)
                        else:
                            print("Author not found")
                if uop == "5": # Update
                    print("")
                if uop == "0": # Log Out
                    logged_in = 0
                    print("User Logged Out")
                else:
                    print("Invalid Operation")
        else:
            print("User not Found")
    # Create User Account
    elif op == "2":
        user_id = f"U{user_counter}"
        user = User(user_id)
        User.add(user)
        user_counter += 1
        all_users.append(user)
    # Browse Books
    elif op == "3":
        for book in all_books:
            print(book)
    # Check Book
    elif op == "4":
        print("1. ID")
        print("2. Title")
        print("0. Back")
        method = input("Choose Search Method: ")
        print("")
        if method == "1":
            find_id = input("Enter Book ID: ")
            found_b = f_book_id(find_id, all_books)
            if found_b:
                author = found_b.a_id
                a_name = f_author_id(author, all_authors)
                Book.display(found_b, a_name)
            else:
                print("Book not found")
        elif method == "2":
            find_title = input("Enter Book Title: ")
            found_b = f_book_title(find_title, all_books)
            if found_b:
                author = found_b.a_id
                a_name = f_author_id(author, all_authors)
                Book.display(found_b, a_name)
            else:
                print("Book not found")
        elif method == "0":
            print("Search Canceled")
        else:
            print("Invalid Operation")
    # Check Author
    elif op == "5":
        print("1. ID")
        print("2. Name")
        print("0. Back")
        method = input("Choose Search Method: ")
        print("")
        if method == "1":
            find_id = input("Enter Author ID: ")
            found_a = f_author_id(find_id, all_authors)
            if found_a:
                Author.display(found_a)
            else:
                print("Author not found")
        elif method == "2":
            find_title = input("Enter Author Name: ")
            found_a = f_author_name(find_title, all_authors)
            if found_a:
                Author.display(found_a)
            else:
                print("Author not found")
        elif method == "0":
            print("Search Canceled")
        else:
            print("Invalid Operation")
    # Check User
    elif op == "6":
        print("1. ID")
        print("2. Username")
        print("3. Address")
        print("0. Back")
        method = input("Choose Search Method: ")
        print("")
        if method == "1":
            find_id = input("Enter User ID: ")
            found_u = f_user_id(find_id, all_users)
            if found_u:
                User.check(found_u)
            else:
                print("User not found")
        elif method == "2":
            find_name = input("Enter Username: ")
            found_u = f_user_name(find_name, all_users)
            if found_u:
                User.check(found_u)
            else:
                print("User not found")
        elif method == "3":
            find_ad = input("Enter User Address: ")
            found_u = f_user_ad(find_ad, all_users)
            if found_u:
                User.check(found_u)
            else:
                print("User not found")
        elif method == "0":
            print("Search Canceled")
        else:
            print("Invalid Operation")
    # Add Book
    elif op == "7":
        book_id = f"U{book_counter}"
        book = Book(book_id)
        Book.add(book)
        book_counter += 1
        all_books.append(book)
    # Add Author
    elif op == "8":
        auth_id = f"U{auth_counter}"
        auth = Author(auth_id)
        Author.add(auth)
        auth_counter += 1
        all_authors.append(auth)
    # End Program
    elif op == "0":
        print ("End Program")
        break
    # Invalid Operation
    else:
        print ("Invalid Operation")
