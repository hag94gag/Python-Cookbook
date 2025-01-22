import random

filp=[]
conin=0
counterH=0
counterT=0
counter=0
for y in range(1001):
    for i in range(100):
        conin=random.randint(0,1)
        if conin==0:
            filp.append("H")
        else:
            filp.append("T")
            
    
    

    for i in filp:
        if i=="H":
            counterH+=1
            counterT=0
            if counterH==6:
                counter+=1
                counterH=0
        else:
            
            counterT+=1
            counterH=0
            if counterT==6:
                counter+=1
                counterT=0
    filp=[]
print(counter)
                