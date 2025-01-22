def calculate (num1,num2,operation:str="add"):
    if operation.lower().strip()=="add" or operation.lower().strip()== "a":
        return num1+num2
    if operation.lower().strip()=="subtract" or operation.lower().strip()== "s":
        return num1-num2
    if operation.lower().strip()=="multiply" or operation.lower().strip()== "m":
        return num1*num2
    else:
        return print("Invalid Operation")



# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200