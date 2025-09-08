a=int(input("Value of A: "))
b=int(input("Value of B: "))
c=int(input("Value of C: "))

if a>b and a>c:
    print("A is the greatest.")
    if b>c:
        print("C is the least.")
    else:
        print("B is the least.")
elif b>a and b>c:
    print("B is the greatest.")
    if a>c:
        print("C is the least.")
    else:
        print("A is the least.")
elif c>a and c>b:
    print("C is the greatest.")
    if b>a:
        print("A is the least.")
    else:
        print("B is the least.")

elif a==c and a==b:
    print("The values are all the same.")
elif a==b:
    print("A and B are both the greatest.")
    print("C is the least.")
elif a==c:
    print("A and C are both the greatest.")
    print("B is the least.")
else:
    print("B and C are both the greatest.")
    print("A is the least.")