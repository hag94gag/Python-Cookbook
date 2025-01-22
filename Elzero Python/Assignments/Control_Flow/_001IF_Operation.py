import sys
nums=input("Enter two numbers: ").strip().split(" ")
for i in nums:
    nums[nums.index(i)]=int(i)
num1=nums[0]
num2=nums[1]
result=0
operation=input("Enter the operation: ").strip()

if num2!=0:
    if operation == "/":
        result=num1/num2
    elif operation == "//":
        result=num1//num2
    elif operation == "%":
        result=num1%num2
else:
    print("The second number can't be zero")
    sys.exit()

if operation == "+":
    result=num1+num2
elif operation == "-":
    result=num1-num2
elif operation == "*":
    result=num1*num2
else:
    print("Invalid operation")
    sys.exit()
    


print (f"Your result is: {result}")