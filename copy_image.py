"""
This script copies a list of image files from a source directory to a target directory.
It verifies the existence of each file in the source directory before copying it to the target directory.

Dependencies:
- shutil: For file copying operations.
- os: For path operations and checking file existence.

Usage:
1. Set 'PATH1' to the path of the source directory containing the image files.
2. Set 'PATH2' to the path of the target directory where the files should be copied.
3. Run the script to copy the specified files.

Developer: Nishant Butani
"""

import shutil
import os

# Define paths
PATH1 = r"E:\2024\whatsapp all\WhatsApp Images"  # Source directory
PATH2 = r"E:\drive\2018\hemu bhabhi ladva"       # Target directory

# List of image filenames to copy
image_filenames = [
    "IMG-20180916-WA0020.jpg", "IMG-20180916-WA0021.jpg", "IMG-20180916-WA0026.jpg",
    "IMG-20180916-WA0033.jpg", "IMG-20180916-WA0038.jpg", "IMG-20180916-WA0039.jpg",
    "IMG-20180916-WA0040.jpg", "IMG-20180916-WA0047.jpg", "IMG-20180916-WA0048.jpg",
    "IMG-20180916-WA0055.jpg", "IMG-20180916-WA0059.jpg", "IMG-20180916-WA0069.jpg",
    "IMG-20180916-WA0088.jpg", "IMG-20180917-WA0007.jpg", "IMG-20180917-WA0017.jpg",
    "IMG-20180917-WA0019.jpg", "IMG-20180917-WA0022.jpg", "IMG-20180917-WA0024.jpg",
    "IMG-20180917-WA0025.jpg", "IMG-20180917-WA0028.jpg", "IMG-20180917-WA0037.jpg",
    "IMG-20180917-WA0066.jpg", "IMG-20180917-WA0067.jpg", "IMG-20180917-WA0079.jpg",
    "IMG-20180917-WA0091.jpg", "IMG-20180917-WA0092.jpg", "IMG-20180917-WA0094.jpg",
    "IMG-20180917-WA0095.jpg", "IMG-20180917-WA0106.jpg", "IMG-20180917-WA0109.jpg",
    "IMG-20180917-WA0111.jpg", "IMG-20180917-WA0117.jpg", "IMG-20180917-WA0118.jpg",
    "IMG-20180917-WA0126.jpg", "IMG-20180917-WA0127.jpg", "IMG-20180917-WA0134.jpg",
    "IMG-20180917-WA0137.jpg", "IMG-20180917-WA0141.jpg", "IMG-20180917-WA0172.jpg",
    "IMG-20180917-WA0180.jpg", "IMG-20180917-WA0183.jpg", "IMG-20180917-WA0190.jpg",
    "IMG-20180917-WA0191.jpg", "IMG-20180917-WA0192.jpg", "IMG-20180917-WA0194.jpg",
    "IMG-20180917-WA0198.jpg", "IMG-20180917-WA0200.jpg"
]

# Iterate over each filename and copy to PATH2
for filename in image_filenames:
    source_file = os.path.join(PATH1, filename)
    if os.path.exists(source_file):
        shutil.copy(source_file, PATH2)
        print(f"Copied {filename} to {PATH2}")
    else:
        print(f"File {filename} not found in {PATH1}")

print("Copying complete.")
