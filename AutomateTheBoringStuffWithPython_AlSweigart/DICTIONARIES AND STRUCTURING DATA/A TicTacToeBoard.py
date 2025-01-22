import random

# Function to print the current game board
def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))  # Join each row's cells with ' | ' and print
        print("-" * 5)  # Print a horizontal line between rows

# Function to check if a player has won
def check_win(board, player):
    """Checks if a given player has won."""
    # Check rows for a win
    for row in board:
        if all([cell == player for cell in row]):  # If all cells in a row match the player
            return True
    
    # Check columns for a win
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):  # If all cells in a column match the player
            return True
    
    # Check diagonals for a win
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True  # Check the two diagonals
    
    return False  # Return False if no win condition is met

# Function to check if the board is full
def check_draw(board):
    """Checks if the board is full (draw)."""
    return all([cell != ' ' for row in board for cell in row])  # Return True if no empty spaces are left

# Function to get the player's move
def get_player_move(board):
    """Prompts the player to enter a valid move."""
    while True:  # Keep asking until a valid move is entered
        try:
            move = int(input("Enter your move (1-9): ")) - 1  # Convert input to index (0-8)
            row, col = divmod(move, 3)  # Get row and column from the move index
            if board[row][col] == ' ':  # Check if the chosen cell is empty
                return row, col  # Return the valid move
            else:
                print("That space is already occupied! Try again.")
        except (ValueError, IndexError):  # Handle invalid inputs
            print("Invalid move! Enter a number between 1 and 9.")

# Function to get a random computer move
def get_computer_move(board):
    """Returns a random valid move for the computer."""
    empty_spaces = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']  # Find all empty cells
    return random.choice(empty_spaces)  # Randomly select an empty cell

# Main function to run the game
def play_game():
    # Initialize the game board (3x3 grid filled with spaces)
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Player starts with 'X'
    is_player_turn = True  # True if it's the player's turn, False if it's the computer's turn
    
    while True:
        print_board(board)  # Print the current state of the board

        if is_player_turn:  # Player's turn
            row, col = get_player_move(board)  # Get the player's move
            board[row][col] = 'X'  # Mark the cell with 'X'
        else:  # Computer's turn
            row, col = get_computer_move(board)  # Get the computer's move
            board[row][col] = 'O'  # Mark the cell with 'O'

        # Check if the current player won
        if check_win(board, 'X'):  # If the player wins
            print_board(board)
            print("Player X wins!")
            break
        elif check_win(board, 'O'):  # If the computer wins
            print_board(board)
            print("Player O (Computer) wins!")
            break

        # Check for a draw
        if check_draw(board):  # If no spaces are left and no winner
            print_board(board)
            print("It's a draw!")
            break

        # Switch turns
        is_player_turn = not is_player_turn  # Alternate between player and computer

# Run the game
if __name__ == '__main__':
    play_game()  # Start the Tic Tac Toe game
