
"""
This script identifies corrupted image files in a specified directory and copies them 
to a separate 'repair' directory for further inspection or repair. It uses the Python 
PIL (Pillow) library to verify image integrity.

Usage:
- Update 'directory_path' with the path to the directory containing the images you want to check.
- Update 'repair_path' with the path to the directory where you want to copy the corrupted images.

Dependencies:
- os
- shutil
- PIL (Pillow)

Developer: Nishant Butani
"""

import os
import shutil
from PIL import Image


class ImageChecker:
    def __init__(self, directory, repair_directory):
        self.directory = directory
        self.repair_directory = repair_directory

    def find_corrupted_images(self):
        """
        Identifies corrupted image files in the specified directory.

        Returns:
            list: A list of filenames of corrupted images.
        """
        corrupted_files = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verify if it's a valid image
            except (IOError, SyntaxError):
                corrupted_files.append(filename)

        return corrupted_files

    def copy_corrupted_images(self, corrupted_images):
        """
        Copies corrupted image files to the repair directory.

        Args:
            corrupted_images (list): A list of filenames of corrupted images.
        """
        if not os.path.exists(self.repair_directory):
            os.makedirs(self.repair_directory)

        for file in corrupted_images:
            source_file = os.path.join(self.directory, file)
            shutil.copy(source_file, self.repair_directory)
            print(f"Copied {file} to {self.repair_directory}")


if __name__ == "__main__":
    # Define the directory containing the images and the repair directory
    directory_path = r'E:\2024\camera\2020'
    repair_path = r"E:\2024\camera\repair"

    # Create an instance of ImageChecker
    checker = ImageChecker(directory_path, repair_path)

    # Find corrupted images
    corrupted_images = checker.find_corrupted_images()

    # Report and copy corrupted images
    if corrupted_images:
        print("Corrupted image files:")
        for file in corrupted_images:
            print(file)
        checker.copy_corrupted_images(corrupted_images)
    else:
        print("No corrupted image files found.")
