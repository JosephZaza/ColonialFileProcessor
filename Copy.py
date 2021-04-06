# Copy copies all of the files from folder to another.

# Import libraries
import os
import shutil

# Set up folder paths
source = "C:\\Users\\Joey's Desktop\\Desktop\\source"
target = "C:\\Users\\Joey's Desktop\\Desktop\\copy"

# Copy all files
src_files = os.listdir(source)
for file_name in src_files:
    full_file_name = os.path.join(source, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, target)
