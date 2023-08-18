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

