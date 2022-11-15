import pathlib
import zipfile

directory = pathlib.Path(r'/Users/kalyakusumadi/Desktop')

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
             comment.replace(' ','_') + '.zip'

with zipfile.ZipFile(r"/Users/kalyakusumadi/backup/pythonzipfile.zip", mode="w") as archive:
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