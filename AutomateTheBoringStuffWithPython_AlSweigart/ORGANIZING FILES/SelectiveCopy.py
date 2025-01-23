import os
import shutil
from pathlib import Path

def selectiveCopy(folder, extensions, destFolder):
    # Check if the destination folder (Distfolder) exists; create it if it doesn't
    os.makedirs(destFolder, exist_ok=True)
    
    # Inside the destination folder, create subfolders for each specified file extension
    for extension in extensions:
        os.makedirs(Path(destFolder) / extension, exist_ok=True)
    
    # Walk through the folder tree starting from the given source folder
    for folders, subfolders, files in os.walk(folder):
        for file in files:
            # Get the file extension by splitting the filename at the last '.' character
            ext = file.split('.')[-1]
            
            # If the file extension matches one of the specified extensions
            if ext in extensions:
                # Copy the file to the corresponding subfolder in the destination folder
                shutil.copy(Path(folders) / file, Path(destFolder) / ext)

# List of extensions to filter and copy
ext = ['pdf', 'jpg', "xlsx", "md", "txt"]

# Call the function with the source folder, list of extensions, and destination folder
selectiveCopy(r"C:\Users\DataCenter\Desktop\Test", ext, r"C:\Users\DataCenter\Desktop\Dist")

                
            