import numpy as np  #numpy is just a multidimensional array

n1 = np.array([10,20,30,40])

print(n1)

print(type(n1))

n2 = np.array([[10,20,30,40],[50,20,100,30]])

print(n2)
print(n2.shape)  #telling me the dimension of n2
n2.shape = (1,8) #here i am telling the dimension to change
print(n2)


n3 = np.zeros((2,2))
print(n3)

n4 = np.full((3,3),5)
print(n4)

n5 = np.arange(10,20)  #arange automatically takes the gap to be of 1 unit
print(n5)

n6 = np.arange(10,20,5)  #here i am telling the gap to be of 5 unit
print(n6)

n7 = np.random.randint(100,200,10)  #here i want to get 10 random integers from the range 100 to 200 exclusive 200
print(n7)

#practicing pandas library

import pandas as pd

d1 = pd.DataFrame({"name" : ["samipa","Guddu","soumendu"],"age": [23,24,24.5]})  #dataframe is a labelled multidimensional data structure
print(d1)

from matplotlib import pyplot as plt

#suicide_df = pd.read_csv('/home/samipa/Downloads/who_suicide_statistics.csv')  #pwd is the comment to get the directory
#print(suicide_df.head())

x = np.arange(1,11)
y = 2*x
plt.plot(x,y,color = 'orange', linewidth = 5)
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#barplot and barplot only takes lists as a input
d1 = {"sam" : 74 , "mike" : 88 , "john" : 98}
name =list(d1.keys())
#print(name)
marks = list(d1.values())
plt.bar(name,marks,color='orange')
plt.show()

#piechart taking lists as inputs

l1 = ['apple','banana','orange','watermelon','guava']
l2 = [70,45,60,90,25]
plt.pie(l2,labels = l1)     #autopct is the command to add percentage
plt.show()

