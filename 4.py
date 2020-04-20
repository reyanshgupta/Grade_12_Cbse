import random
def rando(start,stop):
    numb = []
    for i in range(0,3):
        numb.append(random.randint(start,stop))
    print("Three random numbers in the range are: ",numb)

start = int(input("Enter start number: "))
stop = int(input("Enter last number: "))
rando(start,stop)