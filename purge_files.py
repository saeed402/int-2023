import os
import shutil
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime

# Function to get file owner
def get_file_owner(file_path):
    if os.name == 'nt':
        import ctypes
        from ctypes import wintypes
        GENERIC_READ = 0x80000000
        FILE_SHARE_READ = 0x00000001
        OPEN_EXISTING = 3
        NULL = 0
        INVALID_HANDLE_VALUE = -1
        INVALID_FILE_ATTRIBUTES = -1
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        CreateFileW = kernel32.CreateFileW
        CreateFileW.argtypes = (wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
                                wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE)
        CreateFileW.restype = wintypes.HANDLE
        GetFileInformationByHandle = kernel32.GetFileInformationByHandle
        GetFileInformationByHandle.argtypes = (wintypes.HANDLE, wintypes.LPVOID)
        GetFileInformationByHandle.restype = wintypes.BOOL
        CloseHandle = kernel32.CloseHandle
        CloseHandle.argtypes = (wintypes.HANDLE,)
        CloseHandle.restype = wintypes.BOOL

        hFile = CreateFileW(file_path, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL)
        if hFile == INVALID_HANDLE_VALUE:
            return "Unknown"

        fileInfo = wintypes.BY_HANDLE_FILE_INFORMATION()
        success = GetFileInformationByHandle(hFile, ctypes.byref(fileInfo))
        CloseHandle(hFile)

        if not success:
            return "Unknown"

        sid = fileInfo.nFileIndexHigh << 64 | fileInfo.nFileIndexLow
        return str(sid)

    else:
        import pwd
        return pwd.getpwuid(os.stat(file_path).st_uid).pw_name

# Function to purge files
def purge_files(file_paths):
    purged_records = []  # Initialize an empty list to store purged file records
    
    for file_path in file_paths:
        try:
            backup_path = file_path + ".backup"
            shutil.copy(file_path, backup_path)
            
            original_size = os.path.getsize(file_path)
            original_filename = os.path.basename(file_path)
            last_access_time = datetime.fromtimestamp(os.path.getatime(file_path))
            unique_id = hash(file_path + str(original_size) + str(last_access_time))
            purged_datetime = datetime.now()
            file_owner = get_file_owner(file_path)  # Get the file owner
            
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            
            purged_records.append([file_path, original_size, original_filename, last_access_time, unique_id, purged_datetime, file_owner])  # Add purged file record to the list
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    
    return purged_records  # Return the list of purged file records

# Function to send email with attachments
def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_paths=[]):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    for attachment_path in attachment_paths:
        attachment = open(attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
        message.attach(part)
        attachment.close()

    text = message.as_string()

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def append_records_to_csv(file_path, records):
    with open(file_path, 'a', newline='') as csvfile:  # Use 'a' for append mode
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(records)

if __name__ == "__main__":
    files_to_purge = input("Enter file paths to purge (comma-separated): ").split(',')

    existing_files_to_purge = [file_path for file_path in files_to_purge if os.path.exists(file_path)]
    non_existing_files = [file_path for file_path in files_to_purge if file_path not in existing_files_to_purge]

    if non_existing_files:
        print(f"The following files do not exist: {', '.join(non_existing_files)}")
        
        # Save missing file records to a CSV file
        append_records_to_csv("missing_file_record.csv", [[file_path] for file_path in non_existing_files])
        
        # Exit the program
        exit()
    
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your email password: ")
    receiver_email = input("Enter receiver's email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    # Send email first
    send_email(sender_email, sender_password, receiver_email, subject, body, existing_files_to_purge)
    
    purged_records = purge_files(existing_files_to_purge)
    
    # Save purged file records to the CSV file
    append_records_to_csv("purged_record.csv", purged_records)
