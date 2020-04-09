time1=int(input("Please enter the first time: "))
time2=int(input("Please enter the second time: "))
if time2<time1:
    time2=time2+2360
difference=time2-time1
hours=difference//100
minutes=difference%100
hours=hours+minutes//60
minutes=minutes%60
print(hours, "hours", minutes, "minutes")