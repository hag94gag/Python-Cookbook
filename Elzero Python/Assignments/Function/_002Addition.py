def addition (*nums):
    result=0
    for num in nums:
        if num == 10:
            continue
        elif num == 5 and result >= 5:
            result-=5
        else:
            result+=num
    return result

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160