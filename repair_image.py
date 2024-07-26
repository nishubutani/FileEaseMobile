"""
This script repairs JPEG images in a specified directory. It attempts to open and save each image to
create a new repaired file with '_repaired' appended to the filename. This helps in recovering partially
damaged or corrupted images.

Dependencies:
- os
- PIL (Pillow)

Usage:
1. Set 'directory_path' to the path of the directory containing the JPEG images.
2. Run the script to repair and save images in the directory.

Developer: Nishant Butani
"""

import os
import io
from PIL import Image


def repair_image(file_path):
    """
    Attempts to repair a JPEG image by opening and saving it to a new file with '_repaired' appended to the filename.

    Args:
        file_path (str): The path to the image file to be repaired.
    """
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Open the image using PIL
        with Image.open(io.BytesIO(file_data)) as img:
            repaired_path = file_path.replace(".jpg", "_repaired.jpg")
            img.save(repaired_path)
            print(f"Repaired and saved: {repaired_path}")
    except Exception as e:
        print(f"Could not repair {file_path}: {e}")


def repair_images_in_directory(directory):
    """
    Iterates over all JPEG files in a directory and repairs each one.

    Args:
        directory (str): The path to the directory containing JPEG images.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpg"):  # Ensures case insensitivity for the extension
            file_path = os.path.join(directory, filename)
            repair_image(file_path)


# Set the directory path containing JPEG images to be repaired
directory_path = r'E:\2024\camera\repair'

# Repair images in the specified directory
repair_images_in_directory(directory_path)
