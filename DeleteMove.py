# DeleteMove deletes all contents from one folder and then moves new folders into it.

# Import libraries
import shutil
import os

# Set up folder paths
source = "C:\\Users\\Joey's Desktop\\Desktop\\source"
target = "C:\\Users\\Joey's Desktop\\Desktop\\target"

# Delete all files
for filename in os.listdir(target):
    file_path = os.path.join(target, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print("Failed to delete %s. Reason: %s" % (file_path, e))

# Move all files
file_names = os.listdir(source)
for file_name in file_names:
    shutil.move(os.path.join(source, file_name), target)
