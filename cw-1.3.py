employee = input("Enter employee name: ")
wage = int(input("Hourly wage: "))
hours = int(input("Hours worked each day: "))
days = int(input("Days worked this month: "))
pay = wage * hours * days
print (" ")
print (employee, "should be payed $", pay, "this month.")