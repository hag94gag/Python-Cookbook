def collatz(num):
    """
    Performs the Collatz operation on the given number:
    - If the number is even, divide it by 2 and return the result.
    - If the number is odd, calculate 3 * num + 1 and return the result.
    """
    if num % 2 == 0:  # Check if the number is even
        print(num // 2)  # Print the result of dividing the number by 2
        return num // 2  # Return the result
    else:  # If the number is odd
        print(3 * num + 1)  # Print the result of 3 * num + 1
        return 3 * num + 1  # Return the result

# Prompt the user to input a number
number = int(input("Enter a number"))
# Perform the first Collatz operation
num = collatz(number)

# Continue applying the Collatz operation until the result is 1
while num != 1:
    num = collatz(num)
