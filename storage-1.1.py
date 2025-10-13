# write
file1 = open("test1.txt","w")

file1.write("Hello World!\n")
file1.write("Welcome to OOP class!\n")
file1.write("Have a good time!\n")

file1.close()

# read
file2=open("test1.txt","r")

for line in file2:
    print (line)

file2.close()