def checkstr(a,b):
    lena = len(a)
    lenb = len(b)
    if lena == lenb:
        return True
        
    else:
        return False
        
a = input("Enter 1st String: ")
b = input("Enter 2nd string: ")
checkstr(a,b)