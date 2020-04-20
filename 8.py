def checkunit(x,y):
    modx = x%10
    mody = y%10
    if modx > mody:
        print(x, "has larger unit digit")
    elif mody > modx:
        print(y, "has larger unit digit")
    else:
        print("Both have equal unit digits")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
checkunit(x,y)