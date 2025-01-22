def is_chess(chess: dict):
    """Checks if a given chess board setup is valid."""
    # Define the maximum allowed pieces for each type of chess piece
    Game = \
        {
            "wking": 0,     # White king
            "bking": 0,     # Black king
            "wqueen": 0,    # White queen
            "bqueen": 0,    # Black queen
            
            "wrooks": 0,    # White rooks
            "brooks": 0,    # Black rooks
            "wbishops": 0,  # White bishops
            "bbishops": 0,  # Black bishops
            "wknights": 0,  # White knights
            "bknights": 0,  # Black knights
            
            "wpawns": 0,    # White pawns
            "bpawns": 0     # Black pawns
        }
    
    # Count the occurrences of each piece in the chess dictionary
    for peace in chess.values():
        if peace in Game.keys():  # Check if the piece exists in the allowed Game dictionary
            Game[peace] += 1  # Increment the count of the piece

    # Validate the number of kings and queens for both players
    if Game["wking"] != 1 or Game["bking"] != 1 or Game["wqueen"] != 1 or Game["bqueen"] != 1:
        return False  # Invalid if the count of kings or queens is not exactly 1
    
    # Validate the maximum allowed number of rooks, bishops, and knights
    elif Game["wrooks"] > 2 or Game["brooks"] > 2 or Game["wbishops"] > 2 or Game["bbishops"] > 2 or Game["wknights"] > 2 or Game["bknights"] > 2:
        return False  # Invalid if any of these pieces exceed 2
    
    # Validate the maximum allowed number of pawns
    elif Game["wpawns"] > 16 or Game["bpawns"] > 16:
        return False  # Invalid if any player's pawns exceed 16
    
    else:
        return True  # Valid board setup

# Example of a valid chess board setup
valid_board = {
    "a1": "wrooks",   # White rook at position a1
    "a2": "wpawns",   # White pawn at position a2
    "e1": "wking",    # White king at position e1
    "d1": "wqueen",   # White queen at position d1
    "a8": "brooks",   # Black rook at position a8
    "e8": "bking",    # Black king at position e8
    "d8": "bqueen",   # Black queen at position d8
    "h7": "bpawns"    # Black pawn at position h7
}

# Example of an invalid chess board setup (duplicate black king)
invalid_board = {
    "a1": "wrooks",   # White rook at position a1
    "a2": "wpawns",   # White pawn at position a2
    "e1": "wking",    # White king at position e1
    "d1": "wqueen",   # White queen at position d1
    "a8": "brooks",   # Black rook at position a8
    "e8": "bking",    # Black king at position e8
    "d8": "bqueen",   # Black queen at position d8
    "h7": "bpawns",   # Black pawn at position h7
    "e9": "bking"     # Extra black king at an invalid position (e9)
}

# Update the invalid board to convert piece names to lowercase
updated_board = {}
for place, peace in invalid_board.items():
    updated_board[place] = peace.lower()  # Convert each piece name to lowercase

# Check if the updated board is valid
print(is_chess(updated_board))  # Output: False (because of the extra black king)
