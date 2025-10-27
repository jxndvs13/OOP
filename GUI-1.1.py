import matplotlib.pyplot as plt
import numpy as np

x = np.array(["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"])
y = np.array([21,19,24,17,16,25,24,22,21,21])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

#Line Chart
plt.xlabel("Year")
plt.ylabel("# of...      somethings")
plt.plot(x, y)
plt.show()

#Pie Chart
MyLabels = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]
plt.pie(y, labels=MyLabels)
plt.show()

#Scatter Plot
plt.scatter (x,y)
plt.show()