"""
This script deletes specific image files in a given directory that meet certain criteria.
It targets image files with the ".jpg" extension that have "(2)" in their filenames.

Usage:
- Update 'directory_path' with the path to the directory containing the images you want to delete.

Dependencies:
- os

Developer: Nishant Butani
"""

import os


def delete_specific_images(directory):
    """
    Deletes .jpg files that contain '(2)' in their filenames within the specified directory.

    Args:
        directory (str): The path to the directory containing the images.
    """
    for filename in os.listdir(directory):
        # Check if the file is a .jpg and contains '(2)' in its name
        if filename.endswith(".jpg") and "(2)" in filename:
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")


if __name__ == "__main__":
    # Define the directory containing the images
    directory_path = r'E:\2024\camera\2019'

    # Delete specific images
    delete_specific_images(directory_path)
