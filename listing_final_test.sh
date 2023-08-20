#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 directory email_address"
    exit 1
fi

directory="$1"
email_address="$2"

# Get file size limit from the user
read -p "Enter the minimum file size in KB: " min_size_kb

# Generate file listing with extended details
find "$directory" -type f -exec ls -lh --time-style=long-iso --block-size=1 {} + | \
awk '{split($6, a, "-"); print $1 " , " $3 " , " $5 " , " a[1]"-"a[2]"-"a[3] " , " $NF }' > treefile.csv

# Debugging output
echo "Debugging Output:"
echo "Min Size: $min_size_kb"
echo "File Listing:"
cat treefile.csv

# Filter files based on user input size and extension
awk -F ' , ' -v min_size="$min_size_kb" 'BEGIN { OFS=" , " } $3 > min_size * 1024 && $NF ~ /\.txt$/ { print }' treefile.csv > filtered_files.csv

# Debugging output
echo "Filtered Files:"
cat filtered_files.csv

# Run the Python script to send the email
python3 send_email.py "$email_address" "$min_size_kb"

# Purge selected files
awk -F ' , ' '{ print $NF }' filtered_files.csv | xargs rm -f

echo "Program completed."
