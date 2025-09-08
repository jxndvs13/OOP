name = input("What is your name? ")

course1 = int(input ("Enter grade for course 1, out of 100. "))
course2 = int(input ("Enter grade for course 2, out of 100. "))
course3 = int(input ("Enter grade for course 3, out of 100. "))
course4 = int(input ("Enter grade for course 4, out of 100. "))
course5 = int(input ("Enter grade for course 5, out of 100. "))

total = course1 + course2 + course3 + course4 + course5
average = total / 5
print (" ")
print (name, "your total grade for the five courses is", total, "out of 500 points.")
print ("That is an average score of", average, "in each course.")