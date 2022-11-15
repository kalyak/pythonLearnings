import pathlib
import zipfile
import time
import os

directory = pathlib.Path(r'/Users/kalyakusumadi/Desktop')

target_dir = '/Users/kalyakusumadi/backup'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# The files are backed up into a zip file.
# The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
             comment.replace(' ','_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)  # make subdirectory
    print('Successfully created directory', today)

with zipfile.ZipFile(target, mode="w") as archive:
    errorfiles = []
    for file_path in directory.rglob("*"):
        try:
            archive.write(
                file_path, arcname=file_path.relative_to(directory)
            )
        except FileNotFoundError:
            print(file_path)
            errorfiles.append(file_path)

    print(errorfiles)