import time
Length=int(input("Enter the length of the countdown in seconds "))

def countdown(t):
    while t>0:
        timeformat=divmod(t,60)
        print(timeformat,end='\r')
        time.sleep(1)
        t-=1
    print("Fire in the hole")

countdown(Length)
