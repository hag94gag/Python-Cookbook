import os
from pathlib import Path
import re


def fillGaps(folder):
    FNO = 0  # Variable to track the current file number
    GNO = []  # List to track files that were renamed

    # Walk through the folder tree and find gaps in the numbering
    for foldername, subfoldername, filenames in os.walk(folder):
        # Define a regular expression to match files in the format "Spam###.txt"
        pattern = re.compile(r"^(?P<name>Spam)(?P<number>\d+)(?P<ext>\.txt)$")
        
        # Sort filenames to process them in order
        filenames.sort()

        for file in filenames:
            match = pattern.search(file)  # Match the filename against the pattern
            if match:
                number = int(match.group('number'))  # Extract the number as an integer
                if number == FNO + 1:
                    FNO = number  # No gap, move to the next number
                else:
                    # Record the gap and rename the file to fill it
                    GNO.append(file)
                    new_name = f"Spam{str(FNO + 1).zfill(3)}.txt"
                    os.rename(Path(foldername) / file, Path(foldername) / new_name)
                    FNO += 1
    print(f"Renamed the files to fill the gaps: {GNO}")


def addFile(folder, fileNum):
    # Define a regular expression to match files in the format "Spam###.txt"
    pattern = re.compile(r"^(?P<name>Spam)(?P<number>\d+)(?P<ext>\.txt)$")

    for foldername, subfoldername, filenames in os.walk(folder):
        # Sort filenames to maintain order
        filenames.sort()

        for file in filenames:
            match = pattern.search(file)  # Match the filename against the pattern
            if match:
                number = int(match.group('number'))  # Extract the number as an integer
                if number == fileNum:  # Check if the file with the given number exists
                    # Increment the number and ensure no conflict with existing files
                    new_number = number + 1
                    while Path(foldername) / f"Spam{str(new_number).zfill(3)}.txt" in [
                        Path(foldername) / f for f in filenames
                    ]:
                        new_number += 1
                    new_name = f"Spam{str(new_number).zfill(3)}.txt"
                    os.rename(Path(foldername) / file, Path(foldername) / new_name)
                    print(f"Renamed {file} to {new_name}")
                    return

        # If no file matches the given number, create a new file
        new_file = Path(foldername) / f"Spam{str(fileNum).zfill(3)}.txt"
        if not new_file.exists():
            new_file.touch()  # Create an empty file
            print(f"Created new file: {new_file}")
        else:
            print(f"File {new_file} already exists. Skipping creation.")
        return


# Call the function, providing the path to the folder to check
fillGaps(Path(r"C:\Users\DataCenter\Desktop\Dist"))
addFile(Path(r"C:\Users\DataCenter\Desktop\Dist"), 3)
