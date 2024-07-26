"""
This script deletes files from a source directory if they exist in a search directory.

Usage:
- Update 'source_directory' with the path to the directory containing the files to be deleted.
- Update 'search_directory' with the path to the directory to search for existing files.

Dependencies:
- os

Developer: Nishant Butani
"""

import os

# Define directories
source_directory = "E:\\2024\\whatsapp all\\WhatsApp Images\\2019"
# source_directory will be deleted

search_directory = "E:\\drive\\2020\\meera bhabhi babyshower_2020"

# List all files in the source directory
source_files = os.listdir(source_directory)

# Store the full paths of source files
source_file_paths = [os.path.join(source_directory, file) for file in source_files]


# Function to search for a file in a given directory
def is_file_in_directory(file_name, search_directory):
    """
    Checks if a file exists in the search directory.

    Args:
        file_name (str): The name of the file to search for.
        search_directory (str): The directory to search in.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    for root, dirs, files in os.walk(search_directory):
        if file_name in files:
            return True
    return False


# Iterate over each source file and check if it exists in the search directory
for file_path in source_file_paths:
    file_name = os.path.basename(file_path)
    if is_file_in_directory(file_name, search_directory):
        os.remove(file_path)
        print(f"Deleted: {file_path}")

print("Finished processing files.")
