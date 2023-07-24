#!/usr/bin/env python3
#The os library is used for accessing file attributes.
# navigating the filesystem, and manipulating file paths, ensuring cross-platform compatibility in the Python script.
import os
#it allows the script to read data from and write data to CSV files, making it possible to save the file details in a structured format 
import csv
#It allows the script to parse and process the flags and options provided by the user when running the program
import argparse
#This import method allows us to directly access the datetime class without having to use the module name as a prefix.
from datetime import datetime

def format_file_size(file_size):
    # Convert to MB if file size is greater than or equal to 1 MB
    if file_size >= 1024 * 1024:
        return f"{file_size / (1024 * 1024):.2f} MB"
    # Otherwise, convert to KB
    return f"{file_size / 1024:.2f} KB"

# Function to print file details and save to CSV
def print_file_details(file_path, show_date=False, show_extension=False, show_owner=False, show_size=False):
    file_permissions = oct(os.stat(file_path).st_mode & 0o777)
    file_owner = os.stat(file_path).st_uid
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    abs_path = os.path.abspath(file_path)
    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))

    # Print filename if specified
    if show_extension:
        file_name = os.path.splitext(file_name)[0]
    print(f"Filename: {file_name}")

    # Print file details based on flags
    if show_date:
        print(f"Last Modified: {last_modified}")
    if show_owner:
        print(f"File Owner: {file_owner}")
    if show_size:
        file_size_formatted = format_file_size(file_size)
        print(f"File Size: {file_size_formatted}")
    print(f"File Permissions: {file_permissions}")
    print(f"Absolute Path: {abs_path}")
    print()

    # Save to CSV
    with open("file_details.csv", "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        header = ["File Permissions", "File Owner", "File Size", "Filename", "Absolute Path", "Last Modified"]
        data = [file_permissions, file_owner, file_size, file_name, abs_path, str(last_modified)]
        csv_writer.writerow(data)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Print file details and save to CSV")
parser.add_argument("-d", "--date", action="store_true", help="Show last modified date")
parser.add_argument("-e", "--extension", action="store_true", help="Show filenames without extensions")
parser.add_argument("-o", "--owner", action="store_true", help="Show file owner")
parser.add_argument("-s", "--size", action="store_true", help="Show file size")
args = parser.parse_args()

# Create or truncate the CSV file
with open("file_details.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["File Permissions", "File Owner", "File Size", "Filename", "Absolute Path", "Last Modified"])

# Recursively find files and print their details
for root, _, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        print_file_details(file_path, args.date, args.extension, args.owner, args.size)