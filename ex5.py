# ()# — an empty tuple
# (1.0, 9.9, 10) #— a tuple containing three numeric objects
# ('Casey', 'Darin', 'Bella', 'Mehdi')# — a tuple containing four string objects
# ('10', 101, True) # a tuple containing a string, an integer, and a Boolean object
# # Also, other objects like lists and tuples can comprise a tuple, like this:
# a_tuple = (0, [1, 2, 3], (4, 5, 6), 7.0)
# print(a_tuple)


# numbers = (1, 2, -5)
# print(numbers)


# languages = ('Python', 'Swift', 'C++')
# languages = ('Python', 'Swift', 'C++')
# # access the first item
# print(languages[0])   # Python



# cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# print('Total Items:', len(cars))

a = tuple(range(5))
print(a)

# b = tuple(range(5,10))
# print(b)

# c = tuple(range(0,10,2))
# print(c)

# d = tuple(range(10,0,-2))
# print(d)

# t1 = (2,3,4,5)
# print(sum(t1))

# t3 = (3,4,4,2,2,3,6,7,4,4)
# print(t3.count(4))

# t3 = (3,4,4,2,2,3,6,7,4,4)
# print(t3.index(2))
# print(t3.index(4,3,9))

# t3 = (3,4,4,2,2,3,6,7,4,4)
# print(min(t3))


# numbers = (7, 2, 8, 5, 9)
# print(max(numbers))

# a = (5,6,7,5,5,9,7)
# b = ("a","b","v","b")
# my_tu_1 = tuple(dict.fromkeys(a))
# print(my_tu_1)
# my_tu_2 = tuple(dict.fromkeys(b))
# print(my_tu_2)


# first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
# last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
# ages = (49, 55, 39, 33)
# zipped = tuple(zip(first_names, last_names,ages))
# print(zipped)

# b = ((1,2),(3,4),(5,6))
# my = tuple(item for l in b for item in l)
# print(my)

# t=(1,2,3,4,5,5,13,13,23,2313)
# element=int(input("enter element"))
# sv=t.count(element)
# print(element,"is appear in tupule is",sv)

# t=("1","2","3","4","5","5","13","13","23","2313")
# print("".join(t))

# t=(1,2,3,4,5,13,23,2313)
# print("maximum is",max(t))
# print("minimum is",min(t))

# t=(1,2,3,4,5,13,23,2313)
# element=5
# print("your element is ",element)
# for i in t:
#     if(t.index(i)==element):
#         print("yes element is exist in tupule")

# t=(1,2,3,4,5,13,23,2313)
# print(sorted(t))

# t=(1,2,3,4,5,13,23,2313)
# sv=str(t)
# print(sv)

# t=(1,2,3,4,5,13,23,2313)
# print(t[0])
# print(t[len(t)-1])