import sys
num=int(input("Enter number larger than 0"))
if num <= 0:
    print("The input can't be zero or less")
    sys.exit()
counter=0
while num > 0:
    if num ==611:
        num-=1
        continue
    print (num)
    num-=1
    counter+=1
print(f"{counter} Numbers have been printed")
    