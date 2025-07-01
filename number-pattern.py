#  1      1
#  12    21
#  123  321
#  12344321

n=int(input("enter number of rows :"))
for i in range (n):
    for j in range(1,i+1):
        print(j, end="")
    for j in range(2*(n-i)):
        print(" ", end="") 
    for j in range(i,0,-1):
        print(j, end="")
    print()
