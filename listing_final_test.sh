#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 directory email_address"
    exit 1
fi

directory="$1"
email_address="$2"

# Generate file listing with extended details
find "$directory" -type f -exec ls -lh --time-style=long-iso --block-size=1 {} + | \
awk '{split($6, a, "-"); print $1 " , " $3 " , " $5 " , " a[1]"-"a[2]"-"a[3] " , " $NF }' > treefile.csv

# Filter files based on size and extension
awk -F ' , ' 'BEGIN { OFS=" , " } $3 > 100000 && $NF ~ /\.txt$/ { print }' treefile.csv > filtered_files.csv

# Python script to send email
python3 - <<END
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'your_email@example.com'
receiver_email = '$email_address'
subject = 'Filtered Files Report'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

body = "Filtered files greater than 100KB and with .txt extension:"
msg.attach(MIMEText(body, 'plain'))

# Attach filtered files as attachment
attachment_filename = 'filtered_files.csv'
attachment = open(attachment_filename, 'r').read()
part = MIMEText(attachment, 'csv')
part.add_header('Content-Disposition', f'attachment; filename="{attachment_filename}"')
msg.attach(part)

# Connect to the SMTP server and send the email
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
smtp_username = 'saeed-intr@outlook.com'
smtp_password = 'datascience123'

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully")
END

# Purge selected files
awk -F ' , ' '{ print $NF }' filtered_files.csv | xargs rm -f

echo "Program completed."
