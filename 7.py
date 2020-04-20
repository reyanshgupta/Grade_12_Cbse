import random
def rando(n):
    x = int('9'*(n-1))+1 
    y = int('9'*n)
    ans = random.randint(x,y)
    print("Random number is: ",ans)

n = int(input("Enter the number: "))
rando(n)