"""
This script organizes video files in a specified directory into subdirectories based on the year extracted from their filenames.
The script targets video files following the pattern "VID_yearXXXX_WAXXXX.jpg" and moves them into corresponding year-based folders.

Usage:
- Update 'source_dir' with the path to the directory containing the video files.

Dependencies:
- os
- shutil

Developer: Nishant Butani
"""

import os
import shutil

# Define the source directory containing the images
source_dir = r"E:\2024\camera"

# Get the list of files in the source directory
files = os.listdir(source_dir)
print(files)

# Iterate over each file in the directory
for file in files:
    # Skip the "sent" directory
    if file == "sent" and os.path.isdir(os.path.join(source_dir, file)):
        continue

    # Check if the file follows the pattern VID_yearXXXX_WAXXXX.jpg
    if file.startswith("VID_") and file[4:8].isdigit():
        print("yes")

        # Extract the year from the filename
        year = file[4:8]

        # Define the target subdirectory path
        path2 = "camera video"
        target_dir = os.path.join(source_dir, path2, year)
        print(target_dir)

        # Create the target directory if it does not exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Define the full source and target paths
        source_path = os.path.join(source_dir, file)
        target_path = os.path.join(target_dir, file)

        # Move the file to the target directory
        shutil.move(source_path, target_path)

print("Files have been moved to year-wise folders.")
