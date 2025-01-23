#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)  # Make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):  # If the file doesn't exist, break out of the loop
            break
        number = number + 1

    # Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        
        # Add the current folder to the ZIP file.
        # To avoid adding the folder itself, we append a leading slash.
        backupZip.write(foldername, os.path.basename(foldername))
        
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            # If the file is a backup file (a zip file), skip it.
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # Don't back up the backup ZIP files
                
            backupZip.write(os.path.join(foldername, filename),
                             os.path.relpath(os.path.join(foldername, filename),
                                            os.path.join(folder, '..')))  # Store file with relative path

    # Close the zip file once all files have been added
    backupZip.close()
    print('Done.')

# Specify the folder to back up
backupToZip('C:\\delicious')
