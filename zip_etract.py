"""
Steps to Use ADB for Accessing Files

1. Install ADB:
    - Download and install ADB on your Windows PC. You can download it from the Android developer website.
    - Extract the downloaded ZIP file to a convenient location on your computer.

2. Enable Developer Options and USB Debugging on Your Android Device:
    - Go to Settings > About phone and tap Build number seven times to enable Developer Options.
    - Go to Settings > Developer options and enable USB debugging.

3. Connect Your Android Device:
    - Connect your Android device to your Windows PC using a USB cable and allow USB debugging when prompted on your phone.

4. Verify ADB Connection:
    - Open Command Prompt and run the following command to ensure your device is connected:
        adb devices

5. Run the Script:
    - Update the script with your device ID, paths to the ADB executable, local directory, and Android directory.
    - Save the script in a file, e.g., copy_files.py.
    - Open Command Prompt, navigate to the directory containing copy_files.py, and run the script:
        python copy_files.py
"""

import os
import subprocess
import shutil

# Function to copy files from Android to local directory
def copy_files_from_android(adb_path, device_id, android_directory, local_directory, files):
    count = 0
    for file in files:
        android_file_path = f"{android_directory}/{file}"
        local_file_path = os.path.join(local_directory, file)
        command = [adb_path, '-s', device_id, 'pull', android_file_path, local_file_path]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Copied: {file}")
            count += 1
            print(f"Total files copied: {count}")
        else:
            print(f"Error copying {file}: {result.stderr}")

# Function to list all files in a local directory
def list_local_files(directory):
    return set(os.listdir(directory))

# Function to list all files in a directory on an Android device using adb
def list_android_files(adb_path, device_id, android_directory):
    command = [adb_path, '-s', device_id, 'shell', 'ls', android_directory]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
    if result.returncode == 0:
        return set(result.stdout.splitlines())
    else:
        print("Error:", result.stderr)
        return set()

# Set paths and device ID
device_id = 'b13009b'  # Replace with your actual device ID
adb_path = r'C:\Users\Nishant\Downloads\platform-tools-latest-windows\platform-tools\adb.exe'
local_path1 = r'E:\2024\whatsapp all\WhatsApp Documents'
android_path2 = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp\ Documents/"
android_path3 = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents"

# Get list of files in local and Android directories
local_files = list_local_files(local_path1)
android_files = list_android_files(adb_path, device_id, android_path2)

# Find the count of images in android_files that are not in local_files
unique_android_files = android_files - local_files
unique_count = len(unique_android_files)

print(f"Number of files in '{android_path2}' not in '{local_path1}': {unique_count}")

# Copy unique files from Android to local directory
copy_files_from_android(adb_path, device_id, android_path3, local_path1, unique_android_files)

print("Copying complete.")