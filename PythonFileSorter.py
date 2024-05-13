# This program will take an inputed directory and sort each file into folders based on the file extension
# Developed by Adam Caragine

# shutil allows us to do high level operations on file explorer
import os, shutil

# Path of Folder to be sorted
user_file = input("Insert File Path with / instead of \ and ending in /")
path = user_file

# Get list of file names
file_names = os.listdir(path)

# Find every file extension present in folder and create folders for each
folder_names = []
for file in file_names:
    if os.path.splitext(file)[1] not in folder_names:
        folder_names.append(os.path.splitext(file)[1])

for loop in range(len(folder_names)):
    if not os.path.exists(path + folder_names[loop]):
        os.mkdir(path + folder_names[loop])

for file in file_names:
    ext = os.path.splitext(file)[1]
    shutil.move(path + file, path + ext + "/" + file)