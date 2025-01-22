import sys
age=int(input("Enter you age: "))
if age > 10 and age < 100:
    months=age*12
    weeks=months*4
    days=age*365
    hours=days*24
    minuts=hours*60
    seconds=minuts*60
else:
    print("Your age is out of range")
    sys.exit()
print(months)
print(weeks)
print(days)
print(hours)
print(minuts)
print(seconds)
