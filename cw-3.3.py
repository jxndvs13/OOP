p = int(input("Principle Loan Amount: "))
R = int(input("Rate of Interest: "))
n = int(input("Duration in Years: "))
r=(R/(12*100))

EMI = p * r * ((1 + r) ** n) / ((1 + r) ** n - 1)

for t in range (1,n):
    print ("EMI =", EMI)
    balance = float(p-EMI)
    print ("Balance =", balance)
    p=balance
    print ("-----")
print ("Final payment =", p)