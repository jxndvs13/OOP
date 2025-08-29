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
if average > 100:
    print ("You cheated, you can't get higher than 100")
elif average > 89.5  or average == 89.5:
    print ("Overall grade: A")
    print ("")
    print ("Most excellent")
elif average > 79.5 or average == 79.5:
    print ("Overall grade: B")
    print("")
    print ("Hey, that's pretty good!")
elif average > 69.5 or average == 69.5:
    print ("Overall grade: C")
    print("")
    print ("I mean, it could be worse.")
elif average > 59.5 or average == 59.5:
    print ("Overall grade: D")
    print("")
    print ("You might want to work on that.")
else:
    print ("Overall grade: F")
    print("")
    print ("oof")