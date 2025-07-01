# // 1
# // 22
# // 333
# // 4444
# // 55555

n=int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range(0,i):
        print(i,end=" ")
    print()