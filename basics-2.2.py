n1=int(input("1st number: "))
op=input("Operation: ")
n2=int(input("2nd number: "))

if op == "+" or op == "plus" or op == "add" or op == "sum":
    print ("The sum is:", n1+n2)
elif op == "-" or op == "minus" or op == "subtract" or op == "difference":
    print ("The difference is:", n1-n2)
elif op == "*" or op == "times" or op == "multiply" or op == "product":
    print ("The product is:", n1*n2)
elif op == "/" or op == "divided by" or op == "divide" or op == "quotient":
    print ("The quotient is:", n1/n2)
else:
    print (op, "is not a valid operation.")