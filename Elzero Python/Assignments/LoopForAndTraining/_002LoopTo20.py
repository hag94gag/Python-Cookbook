for i in range(1,21):
    if i  in [6,8,12]:
        continue
    print(str(i).zfill(2))
else:
    print ("all numbers printed")
