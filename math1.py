import random
import math
import time



point=0
numGA=0
numGS=0
numGM=0

print("")
print("---MENTAL CALCULATION GAME---")
print("")
name=str(input("Players name: "))
print("")

def gameOption():
    print("1. Addition Mental Calculation")
    print("2. sustraction Mental Calculation")
    print("3. Multiplication Mental Calculation")
    print("4. Exit")
    ga=int(input("Choose the option number: "))
    if ga==1:
        gameAdd()
    elif ga==2:
        gameSub()
    elif ga==3:
        gameMul()
    else:
        print("if you leave, all your game lists are going to delete")
        k=int(input("Are you sure to leave press '0' or stay '1'"))
        if k==0:
            gameSub()
        else:
            gameOption()


def gameAdd():
    global numGA
    numGA=numGA+1
    point=0
    time.sleep(3)
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
    for i in range(10):
        a=random.randint(1,50)
        b=random.randint(1,50)
        p=time.time()
        c=int(input(f"{a}+{b}="))
        if c==(a+b):
            q=time.time()
            if (q-p)<=7:
                point+=10
            elif (q-p)>7:
                point-=5
        else:
            point-=7
        print(f"Current Point: {point}")
    print("")
    print("--------------------------")
    print("")
    print(f"player:{name}, you got {point} points in your {numGA} game")
    storePADD=[]
    storePADD.append(f"{numGA}:{point}")
    print("")
    print(f"Addition Game list: {storePADD}")
    gameOption()

def gameSub():
    global numGS
    numGS=numGS+1
    point=0
    time.sleep(3)
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
    for i in range(10):
        a=random.randint(1,50)
        b=random.randint(1,50)
        p=time.time()
        c=int(input(f"{a}-{b}="))
        if c==(a-b):
            q=time.time()
            if (q-p)<=7:
                point+=10
            elif (q-p)>7:
                point-=5
        else:
            point-=7
        print(f"Current Point: {point}")
    print("")
    print("--------------------------")
    print("")
    print(f"player:{name}, you got {point} points in your {numGS} game")
    storeSub=[]
    storeSub.append(f"{numGS}:{point}")
    print("")
    print(f"Subtraction Game: {storeSub}")
    gameOption()


def gameMul():
    global numGM
    point=0
    numGM=1+numGM
    time.sleep(3)
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
    for i in range(10):
        a=random.randint(1,12)
        b=random.randint(1,12)
        p=time.time()
        c=int(input(f"{a}x{b}="))
        if c==(a*b):
            q=time.time()
            if (q-p)<=7:
                point+=10
            elif (q-p)>7:
                point-=5
        else:
            point-=7
        print(f"Current Point: {point}")
    print("")
    print("--------------------------")
    print("")
    print(f"player:{name}, you got {point} points in your {numGM} game")
    storeMul=[]
    storeMul.append(f"{numGM}:{point}")
    print("")
    print(f"Multiplication Game: {storeMul}")
    gameOption()

def gameEnd():
    print("Thank you for enjoying the game")


gameOption()













"""time.sleep(3)
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
time.sleep(1)"""

"""while point!=100:
    a=random.randint(1,50)
    b=random.randint(1,50)
    p=time.time()
    c=int(input(f"{a}+{b}="))
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
print(f"player:{name}, did {numG} games to get 100 points")"""



# menu (mental calculation : ADD, Divide, Mul)





