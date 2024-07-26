"""
This script compares files between two directories and deletes duplicates from the second directory if they match the files in the first directory.

Usage:
- Update 'dir1' with the path to the directory containing the reference files.
- Update 'dir2' with the path to the directory from which duplicates should be deleted.

Dependencies:
- os
- filecmp

Developer: Nishant Butani
"""

import os
import filecmp

# Define the directories
dir1 = "E:\\drive\\2018\\Dhruvi-n b_day"
dir2 = "E:\\Google Photos"

# List all files in dir1
files_in_dir1 = os.listdir(dir1)

# Iterate over each file in dir1
for file_name in files_in_dir1:
    file1_path = os.path.join(dir1, file_name)

    # Check if file exists in dir2
    file2_path = os.path.join(dir2, file_name)
    if os.path.exists(file2_path):
        # Compare files
        if filecmp.cmp(file1_path, file2_path, shallow=False):
            # If they are the same, delete the file from dir2
            os.remove(file2_path)
            print(f"Deleted: {file2_path}")

print("Finished checking and deleting files.")
