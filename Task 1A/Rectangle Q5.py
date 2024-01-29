import time
import math
try:
    a=int(input("Enter area: "))
    w=int(math.sqrt(a))
    while(a%w!=0):
        w-=1
    l=[int(a/w),w]
    print(l)
except:
    print()
    print("There seems to be an error!")
finally:
    time.sleep(2)
    exit()
