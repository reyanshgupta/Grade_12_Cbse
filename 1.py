def conversion(dollar,convrate):
    rupee = (dollar*convrate)
    print("Amount in Rupees: ",rupee)

dollar=int(input("Enter Dollars: "))
convrate=int(input("Enter conversion rate: "))
conversion(dollar,convrate)
