#!/usr/bin/env python3

import os
import csv
from datetime import datetime

# Function to print file details and save to CSV
def print_file_details(file_path):
    file_permissions = oct(os.stat(file_path).st_mode & 0o777)
    file_owner = os.stat(file_path).st_uid
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    abs_path = os.path.abspath(file_path)
    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))

    # Print file details
    print(f"File Permissions: {file_permissions}")
    print(f"File Owner: {file_owner}")
    print(f"File Size: {file_size} bytes")
    print(f"Filename: {file_name}")
    print(f"Absolute Path: {abs_path}")
    print(f"Last Modified: {last_modified}")
    print()

    # Save to CSV
    with open(f"{file_name}.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["File Permissions", "File Owner", "File Size", "Filename", "Absolute Path", "Last Modified"])
        csv_writer.writerow([file_permissions, file_owner, file_size, file_name, abs_path, last_modified])

# Recursively find files and print their details
for root, _, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        print(f"Filename: {file}")
        print_file_details(file_path)