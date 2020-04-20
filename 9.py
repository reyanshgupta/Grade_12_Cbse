def series(x,y):
    dist = (y-x)/3
    ans = [x,x+dist,x+(dist*2),y]
    print("The numbers are: ", ans)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
series(x,y)