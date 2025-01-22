friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
if __name__=="__main__":
    poelements=''
    neelements=''
    for i in friends:
        if friends.index(i)%2==0:
            poelements+=i
            poelements+=" "
        else:
            neelements+=i
            neelements+=" "
    print (poelements)
    print (neelements)