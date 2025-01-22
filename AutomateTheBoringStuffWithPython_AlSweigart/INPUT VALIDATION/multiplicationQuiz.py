# Import needed modules
import pyinputplus as pyin  # For validated user input
import random  # For generating random numbers
import time  # For time-related operations (not used in this code)
import re  # For regular expression handling

# Main loop
NumOfQuests = 10  # Total number of math questions to ask
CurrNumOfQuests = 0  # Counter to track the current question number
Oprs = ["-", "*", "/", "+"]  # List of possible math operations

# Continue generating and asking questions until the desired number is reached
while CurrNumOfQuests < NumOfQuests:
    # Generate two random numbers
    CrtRandNum_1 = random.randint(0, 10)  # Random number between 0 and 10
    CrtRandNum_2 = random.randint(1, 10)  # Random number between 1 and 10 (to avoid division by zero)
    CrtRandOpr = random.choice(Oprs)  # Randomly select an operator from the list

    # Perform the appropriate operation based on the randomly chosen operator
    if CrtRandOpr == "-":
        x = CrtRandNum_1 - CrtRandNum_2  # Subtraction
        print(f"{CrtRandNum_1} - {CrtRandNum_2}")
    elif CrtRandOpr == "*":
        x = CrtRandNum_1 * CrtRandNum_2  # Multiplication
        print(f"{CrtRandNum_1} * {CrtRandNum_2}")
    elif CrtRandOpr == "+":
        x = CrtRandNum_1 + CrtRandNum_2  # Addition
        print(f"{CrtRandNum_1} + {CrtRandNum_2}")
    elif CrtRandOpr == "/":
        x = CrtRandNum_1 / CrtRandNum_2  # Division
        print(f"{CrtRandNum_1} / {CrtRandNum_2}")

    # Prompt the user to enter the result of the operation
    try:
        Atp = pyin.inputNum(
            "Enter The Result: ", 
            allowRegexes=[f'^{int(x)}$'],  # Allow only the correct answer
            blockRegexes=[r'.*'],  # Block all other answers
            timeout=30,  # User must answer within 30 seconds
            limit=3  # User has up to 3 attempts to answer correctly
        )
        print("Correct!")  # Inform the user if the answer is correct
    except pyin.TimeoutException:
        # Handle timeout if the user takes too long to respond
        print("Time is up!")
    except pyin.RetryLimitException:
        # Handle the case when the user exceeds the allowed attempts
        print("Out of attempts!")

    # Increment the counter to move to the next question
    CurrNumOfQuests += 1


