grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

# Rotate the grid 90 degrees clockwise
for col in range(len(grid[0])):  # Iterate over the columns
    for row in range(len(grid) - 1, -1, -1):  # Iterate rows from bottom to top
        print(grid[row][col], end='')
    print()  # Move to the next line