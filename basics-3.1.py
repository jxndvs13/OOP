end = int(input("End of Range: "))

for n in range (1,end+1):
    if n%2 == 0:
        print (n, "- even")
    else:
        print (n, "- odd")