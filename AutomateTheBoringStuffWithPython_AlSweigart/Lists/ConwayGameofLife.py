# Import the random module for generating random coordinates
import random

# Initialize a 6x6 grid with empty strings
outerGrid = \
            [
                ['', '', '', '', '', ''],
                ['', '', '', '', '', ''],
                ['', '', '', '', '', ''],
                ['', '', '', '', '', ''],
                ['', '', '', '', '', ''],
                ['', '', '', '', '', '']
            ]

# Initialize a 6x6 grid for tracking changes to the grid
addcord = \
            [
                [0, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ] 

# Variables to store random coordinates
corx = 0
cory = 0

# Populate the grid with 19 random '#' symbols
for i in range(19):
    corx = random.randint(0, 5)  # Random row index
    cory = random.randint(0, 5)  # Random column index
    outerGrid[corx][cory] = "#"  # Place a '#' at the random position

# Infinite loop to simulate grid updates
while True:                  
    # Update the `addcord` grid based on neighboring '#' counts
    for row in range(len(outerGrid)):
        for col in range(len(outerGrid[row])):
            # Calculate the number of neighboring '#' symbols
            neighbors = (
                len(outerGrid[row - 1 if row != 0 else row][col]) +  # Above
                len(outerGrid[row + 1 if row < (len(outerGrid) - 1) else row][col]) +  # Below
                len(outerGrid[row][col - 1 if col != 0 else col]) +  # Left
                len(outerGrid[row][col + 1 if col < (len(outerGrid[row]) - 1) else col])  # Right
            )

            if neighbors >= 3:  # If 3 or more neighbors, mark for addition
                addcord[row][col] = 1
            elif neighbors == 2:  # If exactly 2 neighbors, do nothing
                pass
            elif neighbors < 2:  # If fewer than 2 neighbors, mark for removal
                addcord[row][col] = 0

    # Apply changes to the outerGrid based on the `addcord` grid
    for row in range(len(outerGrid)):
        for col in range(len(outerGrid[row])):
            if addcord[row][col] == 1:  # Add '#' to this cell
                outerGrid[row][col] = "#"
            else:  # Clear this cell
                outerGrid[row][col] = ""

    # Print a visual separator and the current state of the grid
    print("*" * 200)
    print("\n\n\n\n")
    
    # Display the grid row by row
    for i in outerGrid:
        for y in i:
            if y == "":  # If the cell is empty, print a space
                print(" ", end="")
            else:  # If the cell contains '#', print it
                print(y, end="")
        print()  # Move to the next row

    print("\n\n\n\n")
    print("*" * 200)
