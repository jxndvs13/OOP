class Person:
    def __init__(self, nn,nd,ng):
        self.name = nn
        self.DOB = nd
        self.gender = ng
    def display (self):
        print (f"Name: {self.name}")
        print (f"Date of Birth: {self.DOB}")
        print (f"Gender: {self.gender}")
        return "---"

class Student(Person):
    def __init__(self, name,dob,gen,major,id):
        Person.__init__(self,name,dob,gen)
        self.major = major
        self.id = id
    def display(self, Value="", onemore=""):
        print("")
        print(Person.display(self))
        print(f"Major(s): {self.major}")
        print(f"ID: {self.id}")
        if Value != "":
            print("Within Polymorphism:", Value)

S1 = Student("Jaxon","8/3/2007","male","Computer Science & Game Design",42)
S1.display()
S1.display("Look at that")
S1.display("That's Crazy","Wow")