"""
This script searches for directories containing HEIC files within a given directory 
and prints each unique directory path that contains at least one HEIC file.

Usage:
- Update 'directory_path' with the path to the directory you want to search.

Dependencies:
- os

Developer: Nishant Butani
"""

import os


def heic():
    """
    Searches for directories containing HEIC files and prints each unique directory path.
    """

    def print_heic_files(directory_path):
        """
        Walks through the directory and its subdirectories to find HEIC files.

        Args:
            directory_path (str): The root directory to search in.
        """
        unique_paths = set()

        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith('.heic'):
                    unique_paths.add(root)
                    break  # No need to check further files in the same directory

        # Print each unique directory path containing HEIC files
        for path in unique_paths:
            print(path)

    # Example usage
    directory_path = "E:"
    print_heic_files(directory_path)


if __name__ == '__main__':
    heic()
