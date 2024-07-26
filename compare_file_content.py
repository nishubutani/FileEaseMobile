"""
This script compares the content of two specific files to check if they are identical.

Usage:
- Update the paths in 'open' statements with the paths to the files you want to compare.

Dependencies:
- None

Developer: Nishant Butani
"""

# Compare content of two files
with open('E:\\Google Photos\\20170624_170525_1498305454960.jpg', 'rb') as file1, \
     open('E:\\drive\\2017\\Vastrapur lake (dhiren)\\20170624_170525_1498305454960.jpg', 'rb') as file2:
    content1 = file1.read()
    content2 = file2.read()
    if content1 == content2:
        print("Files are identical")
    else:
        print("Files are different")
