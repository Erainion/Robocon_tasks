'''could not find the right interpretation of the leetcode qs
i tried out multiple logics and leetcode was still showing wrong
this logic is working, just not how leetcode wants it to'''

import time
try:
    s=input("Enter string with parentheses: ")
    count=0
    count1=0
    count2=0
    count3=0

    for i in s:
        if(i=='('):
            count1+=1
        elif(i==')' and count1==0):
            count=1
            break
        elif(i==')'):
            count1-=1

        elif(i=='['):
            count2+=1
        elif(i==']' and count2==0):
            count=1
            break
        elif(i==']'):
            count2-=1

        elif(i=='{'):
            count2+=1
        elif(i=='}' and count2==0):
            count=1
            break
        elif(i=='}'):
            count2-=1

    if(count1!=0 or count2!=0 or count3!=0):
        count=1
        
    if(count==0):
      print("true")
    else:
       print("false")
except:
    print()
    print("There seems to be an error!")
finally:
    time.sleep(2)
    exit()


