# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# // // You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# // Example 1:

# // Input: prices = [7,1,5,3,6,4]
# // Output: 5
# // Explanation: Buy on day 2 (price = 1) and 
# // sell on day 5 (price = 6), profit = 6-1 = 5.

# // Note: That buying on day 2 and selling on day 1 
# // is not allowed because you must buy before 
# // you sell.

# // Example 2:

# // Input: prices = [7,6,4,3,1]
# // Output: 0
# // Explanation: In this case, no transactions are 
# // done and the max profit = 0.

import numpy as np
import sys
n=int(input("eneter size of array :"))
max=-sys.maxsize-1
min= sys.maxsize
if n%2==0:
    for x in range(n):
     stock_prices = np.array(int(input("enter value of array :")))
     print(stock_prices)
    for x in range(n):
        for x in range(n):
         if stock_prices[x] > max:
            max = stock_prices[x]
         if stock_prices[x] < min:
            min = stock_prices[x]
    profit = max - min
    print(profit)
else:
    print("this is not possible :")

