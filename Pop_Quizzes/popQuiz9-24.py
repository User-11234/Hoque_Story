import time



print("Hi, please give me a number to count down from! I count to 0.")
num = int(input())

for x in range(num):
    print (num - 1)

    num = (num - 1)
    
    time.sleep(.05)