import math
def nthroot(x,n):
    ans = x**(1/n)
    print(n,"th root of",x,"=",ans)

x = int(input("Enter the number: "))
n = int(input("Enter the number to be raised as root: "))
nthroot(x,n)