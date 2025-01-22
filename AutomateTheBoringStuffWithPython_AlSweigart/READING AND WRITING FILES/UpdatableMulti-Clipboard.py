# Import necessary modules
import shelve  # For persistent storage of data in a dictionary-like format
import pyperclip  # For interacting with the system clipboard (copy/paste)
import sys  # For accessing command-line arguments

# Check if there are more than two arguments passed to the script
if len(sys.argv) > 2:
    # If the user wants to save data from the clipboard
    if sys.argv[1].lower() == "save" or sys.argv[1].lower() == "s":
        # Open the shelve database to store clipboard data
        with shelve.open("Clip") as Cdb:
            Cdb[sys.argv[2]] = pyperclip.paste()  # Save the current clipboard content with the specified key
            print(f"Saved\nas {sys.argv[2]}\n{Cdb[sys.argv[2]]} ")  # Print the saved key and content
    # If the user wants to delete a key-value pair from the database
    elif sys.argv[1].lower() == "delete" or sys.argv[1].lower() == "d":
        # Open the shelve database to delete data
        with shelve.open("clip") as Cdb:
            try:
                del Cdb[sys.argv[2]]  # Attempt to delete the specified key
                print(f"{sys.argv[2]} is deleted")  # Confirm deletion
            except KeyError:
                print(f"No such key: {sys.argv[2]}")  # Print error if the key is not found

# If there is at least one argument passed (other than "save" or "delete")
if len(sys.argv) > 1:
    # If the user wants to list all saved data
    if sys.argv[1].lower() == "list" or sys.argv[1].lower() == "l":
        # Open the shelve database to list all key-value pairs
        with shelve.open("Clip") as Cdb:
            if len(Cdb) == 0:  # Check if the database is empty
                print("Empty")  # Inform the user if the database is empty
            else:
                # Loop through all stored items and print the keys and values
                for k, v in Cdb.items():
                    print(k, v)
    else:
        # If the user wants to retrieve and print data for a specific key
        with shelve.open("Clip") as Cdb:
            try:
                # Retrieve and print the value associated with the given key
                print(f"{sys.argv[1]} :\n{Cdb[sys.argv[1]]} ")
                pyperclip.copy(Cdb[sys.argv[1]])  # Copy the value to the clipboard
            except KeyError as e:
                print(f"The key does not exist {e}")  # Print error if the key does not exist



    

