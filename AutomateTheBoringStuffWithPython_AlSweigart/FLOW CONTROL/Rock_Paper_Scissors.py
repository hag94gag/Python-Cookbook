import random

# Welcome Massege ----------------------------------------------------------------------------
WelMsg=" Welcom to Rock, Paper, Scissors game "
print("\n\n\n")
print("*"*200)
print(f"{WelMsg.center(200,"*")}")
print("*"*200)
print("\n\n\n")
#---------------------------------------------------------------------------------------------

# Initlization of the symobl and the score variables------------------------------------------
Hand=("Rock","Paper","Scissors")
ComputerScore=0
UserScore=0
#---------------------------------------------------------------------------------------------



# The Game loop ==============================================================================
WantsToContinue="yes"
while WantsToContinue=="yes":
    
    ComputerHand=random.choice(Hand) #Set a random value to the Computer
    
    userhand=int(input(f"choose your weapon\n{Hand[0]}->1\n{Hand[1]}->2\n{Hand[2]}->3\n: "))
    if Hand[userhand-1]==ComputerHand:
        print(f"\nYou ----------> {Hand[userhand-1]} VS {ComputerHand} <---------- Me\n")
        print("\nIt's tie\n")
        print(f"The Score is:\nYou {UserScore}\nMe {ComputerScore}\n")
        WantsToContinue=input("Enter yes if you want to play again: ")
        continue
    # The 3 scenarioes you win -------------------------------------------------------------
    elif Hand[userhand-1]=="Rock" and ComputerHand=="Scissors":
        print(f"\nYou ----------> {Hand[userhand-1]} VS {ComputerHand} <---------- Me\n")
        print("\nyou win\n")
        UserScore+=1
        print(f"The Score is:\nYou {UserScore}\nMe {ComputerScore}\n")
        WantsToContinue=input("Enter yes if you want to play again: ")
        continue
    elif Hand[userhand-1]=="Paper" and ComputerHand=="Rock":
        print(f"\nYou ----------> {Hand[userhand-1]} VS {ComputerHand} <---------- Me\n")
        print("\nyou win\n")
        UserScore+=1
        print(f"The Score is:\nYou {UserScore}\nMe {ComputerScore}\n")
        WantsToContinue=input("Enter yes if you want to play again: ")
        continue
    elif Hand[userhand-1]=="Scissors" and ComputerHand=="Paper":
        print(f"\nYou ----------> {Hand[userhand-1]} VS {ComputerHand} <---------- Me\n")
        print("\nyou win\n")
        UserScore+=1
        print(f"The Score is:\nYou {UserScore}\nMe {ComputerScore}\n")
        WantsToContinue=input("Enter yes if you want to play again: ")
        continue
    # ----------------------------------------------------------------------------------------
    else:
        print(f"\nYou ----------> {Hand[userhand-1]} VS {ComputerHand} <---------- Me\n")
        print("\nyou lose\n")
        ComputerScore+=1
        print(f"The Score is:\nYou {UserScore}\nMe {ComputerScore}\n")
        WantsToContinue=input("Enter yes if you want to play again: ")
        continue
# ==================================================================================================

