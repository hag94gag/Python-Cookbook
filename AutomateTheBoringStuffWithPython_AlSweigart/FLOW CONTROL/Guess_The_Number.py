import random#used to generate random numer
import sys #used to exit the application
#the Welcom massege----------------------------------------------------------------------------
Wel_msg=" Welcom to the Guess the number game "
print(f"\n{Wel_msg.center(200,"*")}\n")
#----------------------------------------------------------------------------------------------

#Score Variables
computer=0
user=0

#To loop over the program =======================================================================
wants_to_continue="yes"
while wants_to_continue == "yes":
    #the user input------------------------------------------------------------------------------
    user_range=input("Enter you range of numbers:").split(" ") #Takes two numbers spreated by space
    for i in user_range: # a loop to convert the inputed list into a string
        user_range[user_range.index(i)]=int(i)
    print (f"\nI am thinking of a number between {user_range[0]} and {user_range[1]}.\n")
    #---------------------------------------------------------------------------------------------


    ran_num=random.randint(user_range[0],user_range[1]) #Generate the random number

    #Checking the number---------------------------------------------------------------------------
    wine=False

    while wine==False:
        num=int(input("Enter your num: "))
        if ran_num > num:
            print("Your guess is too low.")
        elif ran_num < num:
            print("Your guess is too high.")
        else:
            print("You got me\n")
            wine=True
            user+=1
            print(f"The score is\n Computer: {computer}\n You: {user}")
    wants_to_continue=input("Enter yes if you wants to continue: ")
    if wants_to_continue!="yes":
        sys.exit()
    #-------------------------------------------------------------------------------------------------
    #=================================================================================================