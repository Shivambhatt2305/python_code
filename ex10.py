# import matplotlib.pyplot as plt 
# import numpy as np
# # data to display on plots 
# x = [3, 1, 3] 
# y = [3, 2, 1] 
# plt.plot(x, y)
# plt.title("Line Chart")
# # Adding the legends
# plt.legend(["Line"])
# plt.show()

# x=np.array([1,2,3,4,5])
# y=x*2
# plt.plot(x,y)
# plt.show()

import matplotlib.pyplot as plt 
import numpy as np 
# x = np.linspace(0.1, 2 * np.pi, 41) 
# y = np.exp(np.sin(x)) 
# plt.stem(x, y) 
# plt.show() 


# data to display on plots 
# x = [3, 1, 3, 12, 2, 4, 4] 
# y = [3, 2, 1, 4, 5, 6, 7] 


# # This will plot a simple bar chart
# plt.bar(x, y)
# # Title to the plot
# plt.title("Bar Chart")
# # Adding the legends
# plt.legend(["bar"])
# plt.show()


# data to display on plots 
# x = [1, 2, 3, 4, 5, 6, 7, 4] 
# # This will plot a simple histogram
# plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])
# # Title to the plot
# plt.title("Histogram")
# # Adding the legends
# plt.legend(["bar"])
# plt.show()


# data to display on plots 
# x = [3, 1, 3, 12, 2, 4, 4]
# y = [3, 2, 1, 4, 5, 6, 7]
# # This will plot a simple scatter chart
# plt.scatter(x, y)
# # Adding legend to the plot
# plt.legend("A")
# # Title to the plot
# plt.title("Scatter chart")
# plt.show()

# np.random.seed(10)
# data = np.random.normal(100, 20, 200)
# fig = plt.figure(figsize =(10, 7))
# # Creating plot
# plt.boxplot(data)

# # show plot
# plt.show()


# data to display on plots 
# x = [1, 2, 3, 4] 
# # this will explode the 1st wedge
# # i.e. will separate the 1st wedge
# # from the chart
# e  =(0.1, 0, 0, 0)
# # This will plot a simple pie chart
# plt.pie(x, explode = e)
# # Title to the plot
# plt.title("Pie chart")
# plt.show()


# # making a simple plot
# x =[1, 2, 3, 4, 5, 6, 7]
# y =[1, 2, 1, 2, 1, 2, 1]
# # creating error
# y_error = 0.2
# # plotting graph
# plt.plot(x, y)
# plt.errorbar(x, y,yerr = y_error,fmt ='o')
# plt.show()

# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# z = [1, 8, 27, 64, 125]
# # Creating the figure object
# fig = plt.figure()
# # keeping the projection = 3d
# # creates the 3d plot
# ax = plt.axes(projection = '3d')
# ax.plot3D(z, y, x)
# plt.show()

# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4, 5] 
# y = [2, 3, 5, 7, 11] 
# plt.plot(x, y) 
# plt.xlabel('X Axis') 
# plt.ylabel('Y Axis') 
# plt.title('Simple Line Plot') 
# plt.show()

# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4, 5] 
# y1 = [2, 3, 5, 7, 11] 
# y2 = [1, 4, 6, 8, 10] 
# plt.plot(x, y1, label='Line 1') 
# plt.plot(x, y2, label='Line 2')
# plt.xlabel('X Axis') 
# plt.ylabel('Y Axis') 
# plt.title('Multiple Lines on Same Plot') 
# plt.legend() 
# plt.show()

import matplotlib.pyplot as plt 
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"] 
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7] 
plt.figure(figsize=(10, 6))  
plt.bar(languages, popularity, color="skyblue", edgecolor="black") 
plt.xlabel("Programming Languages") 
plt.ylabel("Popularity (%)") 
plt.title("Popularity of Programming Languages")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()