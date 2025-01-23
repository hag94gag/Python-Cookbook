import os  # Module for interacting with the operating system
from pathlib import Path  # Module for handling filesystem paths in a more object-oriented way
import send2trash  # Module for sending files to the recycle bin instead of permanently deleting them

def deleteUnneeded(folder):
    # Walk through the folder tree starting at the given folder
    for foldername, subfolders, filenames in os.walk(folder):
        # Iterate over all files in the current folder
        for file in filenames:
            # Check if the file size is greater than 1000 bytes (1KB)
            if os.path.getsize(Path(foldername) / file) > 1000:
                # Print a message indicating the file is larger than the threshold
                print(f'{file} is more than 10MB')  # Note: This comment should say 1KB, not 10MB, based on the condition
                
                # Print an empty line for better readability
                print()
                
                # Send the file to the recycle bin
                send2trash.send2trash(Path(foldername) / file)

# Call the function, providing the path to the folder to check
deleteUnneeded(Path(r"C:\Users\DataCenter\Desktop\Dist"))
