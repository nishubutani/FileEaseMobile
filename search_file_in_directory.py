"""
This script searches for a specific file in a given directory (including its subdirectories)
and lists all paths where the file is found. Optionally, it can compare files to ensure they
are identical.

Usage:
- Update 'source_file' with the path to the file you want to search for.
- Update 'search_directory' with the path to the directory where you want to search.

Dependencies:
- os
- filecmp (optional, if file comparison is enabled)

Developer: Nishant Butani
"""

import os

# import filecmp

# Define the source file path
source_file = "E:\\2024\\camera\\2020\\IMG_20200102_133008.jpg"


def search_file_in_directory(directory, source_file):
    """
    Searches for the specified file in the given directory and its subdirectories.

    Args:
        directory (str): The root directory to search in.
        source_file (str): The full path of the source file to search for.

    Returns:
        list: A list of paths where the file is found.
    """
    found_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == os.path.basename(source_file):
                file_path = os.path.join(root, file)
                # Optionally compare the files to ensure they are the same
                # if filecmp.cmp(source_file, file_path, shallow=False):
                found_paths.append(file_path)
    return found_paths


# Search for the file in the entire E: drive
search_directory = "E:"
matching_paths = search_file_in_directory(search_directory, source_file)

# Print the found paths
for path in matching_paths:
    print(path)

print("Finished searching for the photo.")
