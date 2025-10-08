class Student:
    def __init__(self):
        self.stu_id = ""
        self.stu_name = ""
        self.courses = []
    def add_stu(self):
        self.stu_id = input("Enter Student ID: ")
        self.stu_name = input("Enter Student Name: ")
    def display_stu(self):
        print("Student ID:", self.stu_id)
        print("Student Name:", self.stu_name)
        for x in self.courses:
            print("Courses: ", x.course_name)
    def register_course (self, r1):
        self.courses.append(r1)
class Course:
    def __init__(self):
        self.course_id = ""
        self.course_name = ""
    def add_course(self):
        self.course_id = input("Enter Course ID: ")
        self.course_name = input("Enter Course Name: ")
# Main Code (hardcoded)
s1 = Student()
s1.add_stu()
c1 = Course()
c1.add_course()
c2 = Course()
c2.add_course()
s1.register_course(c1)
s1.register_course(c2)
s1.display_stu()