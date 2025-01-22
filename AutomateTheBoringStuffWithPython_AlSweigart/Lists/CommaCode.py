import sys
def Comma_Code(ls):
    NewWord=""
    for word in ls:
        indx=len(ls)
        if ls.index(word)!=indx-1:
            NewWord+=word+", "
        else:
            NewWord+="and "+word
        
    print(NewWord)




spam=input("Enter your words").split(" ")

if len(spam)>1:

    Comma_Code(spam)
else:
    print("No engh elements")