friends=["Jack","mac","Jhon","thomas","zack","Thomas"]

i=0
counter=0
while i < len(friends):
    if friends[i][0].isupper():
        print(friends[i])
    else:
        counter+=1
    i+=1
else:
    print(f"{counter} Names have not been printed")