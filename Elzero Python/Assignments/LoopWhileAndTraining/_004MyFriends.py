friends=[]
MyFriends=""
MaxFriends=3

trys=0
while trys<4:
    Frin=input("Enter you friend name").strip()
    if Frin.isupper():
        print ("Invalid name")
        Frin=input("Enter you friend name").strip()
    elif Frin.islower:
        msg="the first letter of your name have been converted into capital letter"
        print(msg)
        friends.append(f"{Frin.capitalize} => {msg}")
    else:
        friends.append(Frin)
        print("the name have been added")
    trys+=1
    print(f"you have {4-trys} left")