import time
try:
    print("please enter a positive integer")
    n=int(input("Enter the number of rows: "))
    def fact(n):
        f=1
        for i in range(n):
           f=f*(i+1)
        return f
             
    for i in range(n):
        for j in range(n-i+1):
            print(' ',end="")
        for j in range(i+1):
            print(fact(i)//(fact(j)*fact(i-j)), end=" ")
        print()
except:
    print()
    print("Please enter a valid number")
finally:
    time.sleep(2)
    exit()

'''The code here cannot be directly put in leetcode, this code was made
such that python would run it
The logic for this is using nCr to calculate the row members
(did in midsem cp exam as well)'''
