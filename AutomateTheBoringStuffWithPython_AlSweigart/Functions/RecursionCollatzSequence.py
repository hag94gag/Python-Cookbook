def collatz(num):
    """
    Performs the Collatz operation on the given number:
    - If the number is even, divide it by 2.
    - If the number is odd, calculate 3 * num + 1.
    - Continues recursively until the result is 1.
    """
    if num % 2 == 0:  # Check if the number is even
        result = num // 2  # Divide the number by 2
        print(result)  # Print the result
        if result != 1:  # If the result is not 1, call the function recursively
            return collatz(result)
    else:  # If the number is odd
        result = 3 * num + 1  # Calculate 3 * num + 1
        print(result)  # Print the result
        if result != 1:  # If the result is not 1, call the function recursively
            return collatz(result)

# Prompt the user to enter a number
number = int(input("Enter a number"))
# Call the collatz function with the entered number
num = collatz(number)

