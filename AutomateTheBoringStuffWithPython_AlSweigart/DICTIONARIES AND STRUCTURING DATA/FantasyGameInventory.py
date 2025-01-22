def displayInventory(inventory: dict):
    """Displays the items in the inventory and their counts."""
    print("Inventory:")  # Print the title for the inventory display
    total = 0  # Initialize the total count of items to 0

    # Loop through the inventory dictionary
    for inv, count in inventory.items():
        print(f"{count} {inv}")  # Print the count and name of each item
        total += count  # Add the count of the current item to the total

    print(f"Total number of items: {total}")  # Print the total number of items

# Example inventory dictionary containing items and their respective counts
inventory = {
    'iron sword': 10,        # 10 iron swords
    'wooden shield': 4,      # 4 wooden shields
    'health potion': 25,     # 25 health potions
    'elixir': 8,             # 8 elixirs
    'firebomb': 3,           # 3 firebombs
    'bow': 2,                # 2 bows
    'arrows': 50             # 50 arrows
}

# Call the displayInventory function to print the inventory and total count
displayInventory(inventory)

