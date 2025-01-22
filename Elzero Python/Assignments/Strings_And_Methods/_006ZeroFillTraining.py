num1="18"
num2="8"
num3="7584"
num4="230"
MaxNum=0
NumList=[num1,num2,num3,num4]
for i in NumList:
    if len(i)>MaxNum:
        MaxNum=len(i)
for i in NumList:
    print(i.zfill(MaxNum))