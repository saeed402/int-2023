#Imports necessary modules: The script imports the sys, csv, and os modules for various functionalities.

#Defines the save_to_csv function: This function takes a list of rows and a filename as parameters. It saves the rows to a CSV file with the provided filename.

#Checks command-line arguments: The script checks if the correct number of command-line arguments (only one argument, the input CSV filename) is provided. If not, it prints a usage message and exits.

#Gets the input CSV filename: The script reads the input CSV filename from the command-line argument.

#Initializes the extension_data dictionary: This dictionary will store data about file extensions, including their count and size.

#Reads the input CSV file: The script reads each row from the input CSV file, extracts information like file size and file path, and then extracts the file extension from the file path. It updates the extension_data dictionary with the extension-specific information.

#Calculates total size and prepares table header: The script calculates the total size of all files and prepares a formatted table header.

#Calculates total number of files: The script calculates the total number of files in the data set.

#Prints the header: The formatted table header is printed.

#Displays formatted data in a table: The script iterates through the extension_data dictionary, calculates percentage values for size and count, and prints each extension's information in a formatted row.

#Prints footer line: A line of dashes is printed to indicate the end of the table.

#Asks the user if they want to save data: The script prompts the user whether they want to save the calculated data to a CSV file.

#Handles user's save decision: If the user chooses to save the data, the script prompts the user for a filename and ensures that the filen

#Name has the ".csv" extension. It then checks if the specified file already exists and if not, saves the data to that file using the save_to_csv function.

# Ask user if they want to send the data via email


import sys
import csv
import os
import smtplib
from email.mime.text import MIMEText

# Function to save data to a CSV file
def save_to_csv(rows, filename):
    if not filename.endswith('.csv'):
        filename += '.csv'
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)

# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 myscript.py <input_csv_file>")
    sys.exit(1)

# Get the input CSV filename from command line arguments
input_csv = sys.argv[1]

# Dictionary to store extension data
extension_data = {}

# Read the CSV file
with open(input_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)  # Skip the header

    # Loop through each row in the CSV
    for row in csv_reader:
        _, _, size, _, file_path, _ = row
        extension = os.path.splitext(file_path)[-1]  # Extract file extension
        size = int(size)

        # Update extension data dictionary
        if extension in extension_data:
            extension_data[extension]['count'] += 1
            extension_data[extension]['size'] += size
        else:
            extension_data[extension] = {'count': 1, 'size': size}

# Calculate total size of all files
total_size = sum(ext_info['size'] for ext_info in extension_data.values())

# Prepare table header
table_header = f"{'Extension':<15}{'Size':<12}{'Count':<12}{'Size % ':<12}{'  Count % per ext':<12}"

# Calculate total number of files
total_files = sum(ext_info['count'] for ext_info in extension_data.values())

# Print formatted header
print("")
print('=' * len(table_header))
print(table_header)
print('=' * len(table_header))
print("")

# Display formatted data in a table
for extension, ext_info in extension_data.items():
    ext_size = ext_info['size']
    ext_count = ext_info['count']
    size_percentage = (ext_size / total_size) * 100
    count_percentage = (ext_count / total_files) * 100
    formatted_row = f"{extension:<15}{ext_size:<12}{ext_count:<12}{size_percentage:.2f}%{'':<12}{count_percentage:.2f}%"
    print(formatted_row)

# Print footer line
print('-' * len(table_header))
print("")

# Ask user if they want to save data to a CSV file
save_data = input("Do you want to save the data to a CSV file? (Y/N): ")
if save_data.lower() == 'y':
    while True:
        csv_filename = input("Enter CSV filename to save data: ")
        if not csv_filename.endswith('.csv'):
            csv_filename += '.csv'
        if os.path.exists(csv_filename):
            print("File already exists. Please choose a different filename.")
        else:
            # Save data to the specified CSV file
            with open(csv_filename, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for extension, ext_info in extension_data.items():
                    ext_size = ext_info['size']
                    ext_count = ext_info['count']
                    size_percentage = (ext_size / total_size) * 100
                    count_percentage = (ext_count / total_files) * 100
                    csv_writer.writerow([extension, ext_size, ext_count, f"{size_percentage:.2f}%", f"{count_percentage:.2f}%"])
                print("Data saved to", csv_filename)
                
                # Ask user if they want to send the data via email
send_email = input("Do you want to send the data via email? (Y/N): ")
if send_email.lower() == 'y':
    email_address = input("Enter recipient email address: ")

    # Set up the email server
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587
    sender_email = "saeed-intr@outlook.com"
    sender_password = "datascience123"

    subject = "File Extension Statistics"

    # Prepare the email content
    email_content = []
    email_content.append("")
    email_content.append('=' * len(table_header))
    email_content.append(table_header)
    email_content.append('=' * len(table_header))
    email_content.append("")
    for extension, ext_info in extension_data.items():
        ext_size = ext_info['size']
        ext_count = ext_info['count']
        size_percentage = (ext_size / total_size) * 100
        count_percentage = (ext_count / total_files) * 100
        formatted_row = f"{extension:<15}{ext_size:<12}{ext_count:<12}{size_percentage:.2f}%{'':<12}{count_percentage:.2f}%"
        email_content.append(formatted_row)
    email_content.append('-' * len(table_header))
    email_content.append("")

    # Create the email message
    email_message = MIMEText("\n".join(email_content), "plain")
    email_message["Subject"] = subject
    email_message["From"] = sender_email
    email_message["To"] = email_address

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email_address], email_message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        server.quit()
