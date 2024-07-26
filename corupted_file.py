import os
import shutil

from PIL import Image


def find_corrupted_images(directory):
    corrupted_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            with Image.open(file_path) as img:
                img.verify()  # Verify if it's a valid image
        except (IOError, SyntaxError):
            corrupted_files.append(filename)

    return corrupted_files


directory_path = r'E:\2024\camera\2020'
corrupted_images = find_corrupted_images(directory_path)

if corrupted_images:
    print("Corrupted image files:")
    # for file in corrupted_images:
    #     print(file)
else:
    print("No corrupted image files found.")



# # Define paths
# PATH1 = r"E:\2024\camera\2016"
# PATH2 = directory_path
#
# # Iterate over each filename and copy to PATH2
# for filename in corrupted_images:
#     source_file = os.path.join(PATH1, filename)
#     if os.path.exists(source_file):
#         shutil.copy(source_file, PATH2)
#         print(f"Copied {filename} to {PATH2}")
#     else:
#         print(f"File {filename} not found in {PATH1}")
#
# print("Copying complete.")