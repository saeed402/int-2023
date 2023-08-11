import os  # Import the os module for file operations
import shutil  # Import the shutil module for file operations
import smtplib  # Import the smtplib module for sending emails
from email.mime.multipart import MIMEMultipart  # Import classes for email structure
from email.mime.base import MIMEBase  # Import class for email attachment
from email.mime.text import MIMEText  # Import class for email text
from email import encoders  # Import the encoders module for email attachment

# Function to purge files
def purge_files(file_paths):
    for file_path in file_paths:
        try:
            backup_path = file_path + ".backup"  # Create a backup path by adding ".backup" to the filename
            shutil.copy(file_path, backup_path)  # Copy the original file to the backup path
            
            os.remove(file_path)  # Delete the original file
            print(f"Deleted: {file_path}")  # Print a confirmation message
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")  # Print an error message if deletion fails

# Function to send email with attachments
def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_paths=[]):
    message = MIMEMultipart()  # Create a MIME multipart message
    message['From'] = sender_email  # Set the sender's email address
    message['To'] = receiver_email  # Set the receiver's email address
    message['Subject'] = subject  # Set the email subject
    message.attach(MIMEText(body, 'plain'))  # Attach the email body
    
    for attachment_path in attachment_paths:  # Iterate through attachment paths
        attachment = open(attachment_path, 'rb')  # Open the attachment file in binary mode
        part = MIMEBase('application', 'octet-stream')  # Create a MIMEBase object for the attachment
        part.set_payload(attachment.read())  # Set the attachment content
        encoders.encode_base64(part)  # Encode the attachment
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")  # Set attachment header
        message.attach(part)  # Attach the attachment
        attachment.close()  # Close the attachment file

    text = message.as_string()  # Convert the email message to a string

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)  # Create an SMTP server object
        server.starttls()  # Start a secure connection
        server.login(sender_email, sender_password)  # Log in to the email server
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        server.quit()  # Quit the email server
        print("Email sent successfully!")  # Print a success message
    except Exception as e:
        print(f"Error sending email: {e}")  # Print an error message if sending fails

if __name__ == "__main__":
    files_to_purge = input("Enter file paths to purge (comma-separated): ").split(',')  # Prompt user for file paths separated by commas
    
    existing_files_to_purge = [file_path for file_path in files_to_purge if os.path.exists(file_path)]  # Check for existing files
    non_existing_files = [file_path for file_path in files_to_purge if file_path not in existing_files_to_purge]  # Collect non-existing files
    
    if non_existing_files:
        print(f"The following files do not exist: {', '.join(non_existing_files)}")  # Inform about non-existing files
    else:
        sender_email = input("Enter your email: ")  # Prompt user for sender's email
        sender_password = input("Enter your email password: ")  # Prompt user for sender's password
        receiver_email = input("Enter receiver's email: ")  # Prompt user for receiver's email
        subject = input("Enter email subject: ")  # Prompt user for email subject
        body = input("Enter email body: ")  # Prompt user for email body

        send_email(sender_email, sender_password, receiver_email, subject, body, existing_files_to_purge)  # Send email with attachment
        
        purge_files(existing_files_to_purge)  # Purge the existing files (delete and backup)
