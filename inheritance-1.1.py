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
    def display(self):
        print("")
        print(Person.display(self))
        print(f"Major(s): {self.major}")
        print(f"ID: {self.id}")

class Faculty(Person):
    def __init__(self, name,dob,gen,dept,id,salary):
        Person.__init__(self,name,dob,gen)
        self.dept = dept
        self.id = id
        self.salary = salary
    def display(self):
        print("")
        print(Person.display(self))
        print(f"Department: {self.dept}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")

S1 = Student("Jaxon","8/3/2007","male","Computer Science & Game Design",42)
S1.display()
S2 = Student("Jeff","12/23/2006","male","Some Fake Major",58)
S2.display()
F1 = Faculty("Mr. Stevenson","4/30/1993","male","Engineering","12","$49999.99")
F1.display()