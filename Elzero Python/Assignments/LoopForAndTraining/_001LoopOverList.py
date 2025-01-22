my_nums = [15, 81, 5, 17, 20, 21, 13]
fiveable=[]

for num in my_nums:
    if num %5 == 0:
        fiveable.append(num)
fiveable.sort(reverse=True)
for i in range(len(fiveable)):
    print(f"{i+1} ==> {fiveable[i]}")
else:
    print("All numbers printed")