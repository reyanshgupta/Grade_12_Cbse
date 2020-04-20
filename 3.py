#a
def cube(n):                         
    if n == '':
        print("Since no input provided,")
        print("printing cube of 2,  Cube of 2 is:")
        print(8)
    else:
        x = int(n)
        cuben = x*x*x
        print("Cube of number is: ",cuben)

n = input("Enter number for which cube is to be calculated: ")
cube(n)

#b
def checkequal(a,b):
    if a == b:
        print("Char are equal")
    else:
        print("Not Equal")

a = input("Enter first char: ")
b = input("Enter second char: ")
checkequal(a,b)