x = int(input("Enter day number between 2 & 365 : "))
d = input("Enter first day of the year : ")
l = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
b= x%7 
a = l.index(d)
print(l[a+x%7-1])