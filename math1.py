import random
import math
import time



point=0
numG=0

print("---MENTAL CALCULATION GAME---")
print("If you want to start the game\nplease enter your name")
time.sleep(3)
name=str(input("Players name: "))
print("Let's start the game in 3 seconds")
time.sleep(1)
print("Three")
time.sleep(1)
print("Two")
time.sleep(1)
print("One")
time.sleep(1)
print("Game Start")
time.sleep(1)

while point!=100:
    a=random.randint(1,50)
    b=random.randint(1,50)
    c=int(input(f"{a}+{b}="))
    p=time.time()
    if c==(a+b):
        q=time.time()
        if (q-p)<=7:
            point+=10
        elif (q-p)>7:
            point-=5
    else:
        point-=7
    numG+=1
    print(f"Current Point: {point}")
print(f"player:{name}, did {numG} games to get 100 points")





