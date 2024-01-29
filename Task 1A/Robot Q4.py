import time
try:
    s=input("Enter moves: ")
    v=0
    h=0

    for i in s:
        if(i=='U' or i=='u'):
            v+=1
        elif(i=='D' or i=='d'):
            v-=1
        elif(i=='R' or i=='r'):
            h+=1
        elif(i=='L' or i=='l'):
            h-=1

    if(v==0 and h==0):
        print("true")
    else:
        print("false")
except:
    print()
    print("There seems to be an error!")
finally:
    time.sleep(2)
    exit()
