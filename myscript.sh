#!/bin/bash

# Function to display help message
function display_help {
    echo "Usage: $0 <file_abs_path> [options]"
    echo "Options:"
    echo "  -d, --date               Show last modified date"
    echo "  -s, --size <size>        Show files with size greater than or equal to <size>"
    echo "                           Accepted formats: B, KB, MB, GB, TB"
    echo "  -u, --username <owner>   Show files owned by the specified <owner>"
    echo "  -e, --extension          Show filenames without extensions"
    echo "  -h, --help               Show this help message"
    echo "Example: $0 <file_abs_path> -s 1KB"
}

# Function to convert human-readable size to bytes
function to_bytes {
    local input=$1
    local unit=${input: -2}
    local value=${input:0: -2}

    case $unit in
        KB) echo "$((value * 1024))";;
        MB) echo "$((value * 1024 * 1024))";;
        GB) echo "$((value * 1024 * 1024 * 1024))";;
        TB) echo "$((value * 1024 * 1024 * 1024 * 1024))";;
        *) echo "$input";;
    esac
}

# Function to filter file details based on the given flags
function filter_file_details {
    local file_path="$1"
    local show_date="$2"
    local show_size="$3"
    local show_owner="$4"
    local show_extension="$5"

    # Size filter in bytes
    local size_filter_bytes
    if [[ -n "$size_filter" ]]; then
        size_filter_bytes=$(to_bytes "$size_filter")
    fi

    # Print header
    echo "File Permissions,File Owner,File Size,Filename,Absolute Path,Last Modified"

    # Read file details from CSV and apply filters
    while IFS=, read -r file_permissions file_owner file_size file_name abs_path last_modified; do
        # Skip the header row
        if [[ "$file_permissions" == "File Permissions" ]]; then
            continue
        fi

        # Apply filters based on flags
        if [[ "$show_size" == "true" && ($file_size -lt $size_filter_bytes) ]]; then
            continue
        fi
        if [[ "$show_owner" == "true" && "$file_owner" != "$owner_filter" ]]; then
            continue
        fi
        if [[ "$show_extension" == "true" ]]; then
            file_name="${file_name%.*}"
        fi

        # Print the details in the desired format
        echo "$file_permissions,$file_owner,$file_size,$file_name,$abs_path,$last_modified"
    done <"$file_path"
}


# Check if the file path is provided as an argument
if [[ $# -eq 0 ]]; then
    display_help
    exit 1
fi

# Parse command-line arguments
file_path="$1"
size_filter=""
owner_filter=""
show_date="false"
show_size="false"
show_owner="false"
show_extension="false"

while [[ $# -gt 1 ]]; do
    case "$2" in
    -d | --date)
        show_date="true"
        shift
        ;;
    -s | --size)
        show_size="true"
        size_filter="$3"
        shift 2
        ;;
    -u | --username)
        show_owner="true"
        owner_filter="$3"
        shift 2
        ;;
    -e | --extension)
        show_extension="true"
        shift
        ;;
    -h | --help)
        display_help
        exit 0
        ;;
    *)
        echo "Unknown option: $2"
        display_help
        exit 1
        ;;
    esac
done

# Validate size filter input
if [[ "$show_size" == "true" && -n "$size_filter" ]]; then
    size_filter_bytes=$(to_bytes "$size_filter")
    if [[ -z "$size_filter_bytes" ]]; then
        echo "Invalid size format: $size_filter"
        exit 1
    fi
fi

# Validate owner filter input
if [[ "$show_owner" == "true" && -z "$owner_filter" ]]; then
    echo "Owner filter requires a username argument"
    exit 1
fi

# Check if the file exists
if [[ ! -f "$file_path" ]]; then
    echo "File not found: $file_path"
    exit 1
fi

# Call the filter_file_details function to display filtered file details
filter_file_details "$file_path" "$show_date" "$show_size" "$show_owner" "$show_extension"