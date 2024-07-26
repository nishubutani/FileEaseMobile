"""
This script demonstrates how to use ADB (Android Debug Bridge) to interact with an Android device.
It covers setting up ADB, enabling developer options on your Android device, connecting the device,
and running commands to list files and manage files between the local system and the Android device.

Prerequisites:
1. Install ADB:
   - Download and install ADB on your Windows PC from the Android developer website.

2. Enable Developer Options and USB Debugging on Your Android Device:
   - Go to Settings > About phone and tap 'Build number' seven times to enable Developer Options.
   - Go to Settings > Developer options and enable 'USB debugging'.

3. Connect Your Android Device:
   - Connect your Android device to your Windows PC using a USB cable and allow USB debugging when prompted on your phone.

Commands to Verify ADB Connection:
1. Open Command Prompt and run:
   - `adb version`: To check the ADB version.
   - `adb devices`: To list connected devices.

Example Python Code:
- Lists files in a specified directory on the Android device.
"""

import subprocess
import os


def adb_version(adb_path):
    """
    Checks the ADB version.

    Args:
        adb_path (str): The path to the ADB executable.
    """
    command = [adb_path, 'version']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("ADB Version:")
        print(result.stdout)
    else:
        print("Error:", result.stderr)


def list_android_files(adb_path, device_id, android_directory):
    """
    Lists all files in a specified directory on the Android device.

    Args:
        adb_path (str): The path to the ADB executable.
        device_id (str): The ID of the Android device.
        android_directory (str): The directory path on the Android device.

    Returns:
        set: A set of filenames in the specified directory on the Android device.
    """
    command = [adb_path, '-s', device_id, 'shell', 'ls', android_directory]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
    if result.returncode == 0:
        return set(result.stdout.splitlines())
    else:
        print("Error:", result.stderr)
        return set()


def adb_devices(adb_path):
    """
    Lists connected Android devices.

    Args:
        adb_path (str): The path to the ADB executable.
    """
    command = [adb_path, 'devices']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Connected Devices:")
        print(result.stdout)
    else:
        print("Error:", result.stderr)


def main():
    # Set the path to the ADB executable
    adb_path = r'C:\Users\Nishant\Downloads\platform-tools-latest-windows\platform-tools\adb.exe'

    # Set the device ID (replace with your actual device ID)
    device_id = 'YOUR_DEVICE_ID_HERE'

    # Set the Android directory path
    android_directory = '/sdcard/DCIM/Camera'

    # Verify ADB connection
    adb_devices(adb_path)

    # Check ADB version
    adb_version(adb_path)

    # List files in the Android directory
    print(f"Listing files in {android_directory}:")
    android_files = list_android_files(adb_path, device_id, android_directory)
    for file in android_files:
        print(file)


if __name__ == '__main__':
    main()
