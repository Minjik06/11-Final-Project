import random
import time



point=0
numGA=0
numGS=0
numGM=0
numGD=0
storePADD=[]
storeP=[]
storeSub=[]
storeS=[]
storeMul=[]
storeM=[]
storeDiv=[]
storeD=[]

print("")
print("---MENTAL CALCULATION GAME---")
print("")
name=str(input("Players name: "))
print("")

def gameOption():
    print("1. Addition Mental Calculation")
    print("2. sustraction Mental Calculation")
    print("3. Multiplication Mental Calculation")
    print("4. Division Mental Calulation")
    print("5. Exit")
    ga=int(input("Choose the option number: "))
    if ga==1:
        gameAdd()
    elif ga==2:
        gameSub()
    elif ga==3:
        gameMul()
    elif ga==4:
        gameDiv()
    else:
        print("")
        print("NOTICE:")
        print("if you leave, all your game lists are going to delete")
        k=int(input("Are you sure to leave press '0' or stay '1'"))
        if k==0:
            gameEnd()
        else:
            gameOption()


def gameAdd():
    global numGA
    numGA=numGA+1
    point=0
    time.sleep(2)
    print("")
    print("Let's start the game in 3 seconds")
    time.sleep(1)
    print("Three")
    time.sleep(1)
    print("Two")
    time.sleep(1)
    print("One")
    time.sleep(1)
    print("Game Start!!!!!")
    print("")
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
    print("")
    print("--------------------------")
    print("")
    print(f"player: {name}, you got {point} points in your {numGA} game")
    storePADD.append(f"Game: {numGA} -> {point}")
    storeP.append(point)
    print("")
    print(f"Addition Game score list: {storePADD}")
    print("")
    print("--------------------------")
    gameOption()

def gameSub():
    global numGS
    numGS=numGS+1
    point=0
    time.sleep(2)
    print("")
    print("Let's start the game in 3 seconds")
    time.sleep(1)
    print("Three")
    time.sleep(1)
    print("Two")
    time.sleep(1)
    print("One")
    time.sleep(1)
    print("Game Start!!!!!")
    print("")
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
    print("")
    print("--------------------------")
    print("")
    print(f"player: {name}, you got {point} points in your {numGS} game")
    storeSub.append(f"Game: {numGS} -> point : {point}")
    storeS.append(point)
    print("")
    print(f"Subtraction Game socre list: {storeSub}")
    print("")
    print("--------------------------")
    gameOption()


def gameMul():
    global numGM
    point=0
    numGM=1+numGM
    time.sleep(2)
    print("")
    print("Let's start the game in 3 seconds")
    time.sleep(1)
    print("Three")
    time.sleep(1)
    print("Two")
    time.sleep(1)
    print("One")
    time.sleep(1)
    print("Game Start!!!!!")
    print("")
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
    print("")
    print("--------------------------")
    print("")
    print(f"player: {name}, you got {point} points in your {numGM} game")
    storeMul.append(f"Game: {numGM} -> point : {point}")
    storeM.append(point)
    print("")
    print(f"Multiplication Game score list: {storeMul}")
    print("")
    print("--------------------------")
    gameOption()



def gameDiv():
    global numGD
    point=0
    numGD=1+numGD
    print("")
    print("Do not need decimal point")
    time.sleep(2)
    print("")
    print("Let's start the game in 3 seconds")
    time.sleep(1)
    print("Three")
    time.sleep(1)
    print("Two")
    time.sleep(1)
    print("One")
    time.sleep(1)
    print("Game Start!!!!!")
    print("")
    time.sleep(1)
    for i in range(10):
        a=random.randint(50,200)
        b=random.randint(1,30)
        p=time.time()
        c=int(input(f"{a}/{b}="))
        if c==int(a/b):
            q=time.time()
            if (q-p)<=10:
                point+=10
            elif (q-p)>10:
                point-=5
        else:
            point-=7
        print(f"Current Point: {point}")
        print("")
    print("")
    print("--------------------------")
    print("")
    print(f"player: {name}, you got {point} points in your {numGD} game")
    storeDiv.append(f"Game: {numGD} -> point : {point}")
    storeD.append(point)
    print("")
    print(f"Multiplication Game score list: {storeDiv}")
    print("")
    print("--------------------------")
    gameOption()



large=0
large1=0
large2=0
large3=0
def gameEnd():
    global large
    global large1
    global large2
    global large3
    if len(storeP)!=0:
        i=0
        large=storeP[i]
        for i in range(len(storeP)-1):
            if storeP[i]<storeP[i+1]:
                large=storeP[i+1]
        print("")
        print(f"Highest Point in ADDITION: {large}")
    if len(storeS)!=0:
        i=0
        large1=storeS[i]
        for i in range(len(storeS)-1):
            if storeS[i]<storeS[i+1]:
                large1=storeS[i+1]
        print("")
        print(f"Highest Point in SUBTRACTION: {large1}")
    if len(storeM)!=0:
        i=0
        large2=storeM[i]
        for i in range(len(storeM)-1):
            if storeM[i]<storeM[i+1]:
                large2=storeM[i+1]
        print("")
        print(f"Highest Point in MULTIPLICATION: {large2}")
    if len(storeD)!=0:
        i=0
        large3=storeD[i]
        for i in range(len(storeD)-1):
            if storeD[i]<storeD[i+1]:
                large3=storeD[i+1]
        print("")
        print(f"Highest Point in DIVISION: {large3}")

    time.sleep(2)

    print("")
    print("<<Thank you for enjoying the Mental Calculation game>>")


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





