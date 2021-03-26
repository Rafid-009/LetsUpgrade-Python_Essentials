import random

#Assigning Runway
n = random.randint(0,12)


print('Hi Captain, this ground control from YOYO Airport. You are estimately 5000 km from us.\n')


def Check(alt):
    if alt >= 6000:
        print("You are leaving our airspace. Good Luck.")
    elif alt<=3000 :
        print("Captain you are clear to land. Runway", n, "is clear and lit for you.")
    else:
        print("Please maintain 3000 altitude for landing clearence.\n")
        Recheck()

def Start():
    Check(int(input('Please input your current altitude : ')))
def Recheck():
    Start()
    
#Launches the Program
Start()
