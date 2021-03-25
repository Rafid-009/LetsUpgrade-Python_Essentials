print('Hi Captain, this ground control from YOYO Airport. You are estimately 5000 km from us.')
alt = int(input('Please input your current altitude : '))

if alt >= 6000:
    print("You are leaving our airspace. Good Luck.")
elif alt<=3000 :
    print("Captain you are clear to land. Runway 5 is clear and lit for you.")
else:
    print("Please maintain 3000 altitude for landing clearence.\n")
    alt = int(input('Please input your current altitude : '))
    if alt >= 6000:
        print("You are leaving our airspace. Good Luck.")
    elif alt<=3000 :
        print("Captain, you are clear to land. Runway 5 is clear and lit for you.")
    else:
        print("Please maintain 3000 altitude for landing clearence./n")
