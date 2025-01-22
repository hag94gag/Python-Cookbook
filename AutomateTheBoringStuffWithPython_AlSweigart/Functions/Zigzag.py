def Zigzag():
    """
    Creates an infinite zigzag animation by repeatedly printing asterisks (*) 
    moving left to right and then back from right to left in a wave-like motion.
    """
    while True:  # Infinite loop to keep the animation running
        # Move the asterisks (*) from left to right
        for i in range(0, 50):  # Loop from 0 to 49
            print(" " * i, end="")  # Print spaces to create the indentation
            print("*******")  # Print the asterisks (*)
            if i == 49:  # When the asterisks reach the far right
                # Move the asterisks (*) back from right to left
                for i in range(48, -1, -1):  # Loop from 48 back to 0
                    print(" " * i, end="")  # Print spaces for indentation
                    print("*******")  # Print the asterisks (*)

# Call the Zigzag function to start the animation
Zigzag()


