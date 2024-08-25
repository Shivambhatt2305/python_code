# #write a python program to find the sum of unit digit in the number of given list12=[25,36]=11
# list=[25,36]
# sum=0
# for l in list:
#     l=l%10
#     sum=sum+l
# print(sum)

# #write a program to filter even and odd number from a list
# list=[2,3]
# for list2 in list:
#     if list2%2!=0:
#         l=list2
# print(l)
# for list3 in list:
#     if list3%2==0:
#         l1=list3
# print(l1)

# wrp to handle a zerodivision error exception when dividing a number zero
# n=int(input("enter numerator"))
# d=int(input("enter dinomineter"))
# if d==0:
#         print("zerodivision error exception")
# else:
#         print(n/d)

# #wrp maximum of three number
# def max(s,v,a):
#     if s>v & s>a:
#         print(s)
#     elif v>s & v>a:
#         print(v)
#     else:
#         print(a)
    
# s=int(input("enter 1st number"))
# v=int(input("enter 2st number"))
# a=int(input("enter 3st number"))
# max(s,v,a)

# show to extract all number between a given range from a numpy array
# import numpy as np
# a = np.array([2, 6, 1, 9, 10, 3, 27])
# lower_limit = 5
# upper_limit = 11
# answer = a[(a >= lower_limit) & (a <= upper_limit)]
# print(answer)

# #wrp to find missing number in list
# list=[1,2,5,10,11,14,17,20]
# flag =0
# for e in range(1,max(list)):
#     flag=0
#     for e1 in list:
#         if(e==e1):
#             flag=1
#     if(flag==0):
#         print(e)


# list=[12,23]
# mul=1
# for l in list:
#     l=l%10
#     mul=mul*l
# print(mul)

# #how to reverse of 2d array
# # import numpy as np
# # a=np.array([[0,1,2],
# #            [3,4,5],
# #            [6,7,8]])
# # new_array=np.fliplr(a)
# # print(new_array)

# # #how to reverse the columns of a 2D array?
# # import numpy as np
# # my_array = np.array([[1,2,3],
# #                      [4,5,6],
# #                      [7,8,9]])
# # reversed_array = np.fliplr(my_array)
# # print(reversed_array)

# # write a python program to generate 100HZ discreate sine wave and plot
# # import numpy as np
# # import matplotlib.pyplot as plt
# # a=100
# # b= np.linspace(0, 10, 100) 
# # sine_wave = np.sin(2 * np.pi * a * b)
# # plt.stem(b, sine_wave)
# # plt.title('100Hz Discrete Sine Wave')
# # plt.xlabel('Time [s]')
# # plt.ylabel('Amplitude')
# # plt.grid(True)
# # plt.show()

