import pickle

d={"stu1": {"Name": "Jaxon", "Age": "18", "ID": "1"},
   "stu2": {"Name": "Ethan", "Age": "17", "ID": "2"},
   "stu3": {"Name": "Jimmy", "Age": "18", "ID": "3"}}

with open("myUsers.pkl", "wb") as file1:
    pickle.dump(d, file1)
file1.close()

with open("myUsers.pkl", "rb") as file2:
    myDictionary = pickle.load(file2)

i=1
for x in myDictionary:
    var = "stu"+str(i)
    print(myDictionary[var]["Name"])
    i += 1