#!/bin/bash
# Function to display help message
# This function prints the usage and available options of the script.

# Function to convert human-readable size to bytes
# This function takes a human-readable size input (e.g., 1KB) and converts it to bytes.

# Function to convert bytes to human-readable size
# This function takes a size in bytes and converts it to a human-readable format (e.g., KB, MB).

# Function to filter file details based on the given flags
# This function reads file details from a CSV file and applies filters based on the provided flags.
# The filters include size, date, owner, and extension. It can show individual file details or a listing.

# Check if the file path is provided as an argument
# This part of the script checks if the user provided the file path as an argument. If not, it displays the help message.

# Parse command-line arguments
# This part of the script parses the command-line arguments and sets the appropriate variables based on the provided flags.

# Check if the file exists
# This part of the script checks if the input file exists. If not, it displays an error message and exits.

# Call the filter_file_details function to display filtered file details
# This part of the script calls the filter_file_details function with the provided arguments to display the filtered file details.
# Function to display help message
function display_help {
    echo "Usage: $0 <file_abs_path> [options]"
    echo "Options:"
    echo "  -s, --size <size>        Show files with size greater than or equal to <size>"
    echo "                           Accepted formats: B, KB, MB, GB, TB"
    echo "  -d, --date <YYYY-MM-DD>  Show files with modification date equal to <YYYY-MM-DD>"
    echo "  -o, --owner <owner>      Show files owned by the specified <owner>"
    echo "  -e, --extension          Show filenames without extensions"
    echo "  -l, --listing            Show file listing instead of individual files"
    echo "  -h, --help               Show this help message"
    echo "Example: $0 <file_abs_path> -s 1KB"
}

# Function to convert human-readable size to bytes
function human_readable_size_to_bytes {
    local input=$1

    # Convert input to lowercase for case-insensitivity
    input=$(echo "$input" | tr '[:upper:]' '[:lower:]')

    # Extract numeric value and unit from input
    local numeric_value=${input//[!0-9]/}
    local unit=${input//[0-9]/}

    case $unit in
        b) echo "$numeric_value";;
        kb) echo "$((numeric_value * 1024))";;
        mb) echo "$((numeric_value * 1024 * 1024))";;
        gb) echo "$((numeric_value * 1024 * 1024 * 1024))";;
        tb) echo "$((numeric_value * 1024 * 1024 * 1024 * 1024))";;
        *) echo "Invalid size format: $input"; exit 1;;
    esac
}

# Function to convert bytes to human-readable size
function bytes_to_human_readable_size {
    local bytes=$1

    if (( bytes < 1024 )); then
        echo "${bytes}B"
    elif (( bytes < 1048576 )); then
        echo "$(( bytes / 1024 ))KB"
    elif (( bytes < 1073741824 )); then
        echo "$(( bytes / 1024 / 1024 ))MB"
    else
        echo "$(( bytes / 1024 / 1024 / 1024 ))GB"
    fi
}

# Function to filter file details based on the given flags
function filter_file_details {
    local file_path="$1"
    local size_filter="$2"
    local date_filter="$3"
    local owner_filter="$4"
    local show_extension="$5"
    local show_listing="$6"

    # Convert size_filter to bytes (if required)
    local size_filter_bytes
    if [[ -n "$size_filter" ]]; then
        size_filter_bytes=$(human_readable_size_to_bytes "$size_filter")
    fi

    # Print header for individual files or listing
    if [[ "$show_listing" == "true" ]]; then
        printf "%-30s %-20s %-12s %-20s %-10s\n" "Filename" "Owner" "Last Modified" "File Size" "Extension"
        printf "%s\n" "--------------------------------------------------------------------------------"
    else
        printf "%-30s %-50s %-12s\n" "Filename" "Absolute Path" "Last Modified"
        printf "%s\n" "------------------------------------------------------------"
    fi

    # Read file details from CSV and apply filters
    while IFS=, read -r file_permissions file_owner file_size file_name abs_path last_modified; do
        # Skip the header row
        if [[ "$file_permissions" == "File Permissions" ]]; then
            continue
        fi

        # Apply filters based on flags
        if [[ -n "$size_filter" && ($file_size -lt $size_filter_bytes) ]]; then
            continue
        fi
        if [[ -n "$date_filter" && "$last_modified" != "$date_filter" ]]; then
            continue
        fi
        if [[ -n "$owner_filter" && "$file_owner" != "$owner_filter" ]]; then
            continue
        fi
        if [[ "$show_extension" == "true" ]]; then
            file_name="${file_name%.*}"
        fi

        # Format the output for individual files or listing
        if [[ "$show_listing" == "true" ]]; then
            file_extension="${file_name##*.}"
            file_size_human=$(bytes_to_human_readable_size "$file_size")
            printf "%-30s %-20s %-12s %-20s %-10s\n" "$file_name" "$file_owner" "$last_modified" "$file_size_human" "$file_extension"
        else
            printf "%-30s %-50s %-12s\n" "$file_name" "$abs_path" "$last_modified"
        fi
    done < "$file_path"
}

# Check if the file path is provided as an argument
if [[ $# -eq 0 ]]; then
    display_help
    exit 1
fi

# Parse command-line arguments
file_path="$1"
size_filter=""
date_filter=""
owner_filter=""
show_extension="false"
show_listing="false"

while [[ $# -gt 1 ]]; do
    case "$2" in
    -s | --size)
        size_filter="$3"
        shift 2
        ;;
    -d | --date)
        date_filter="$3"
        shift 2
        ;;
    -o | --owner)
        owner_filter="$3"
        shift 2
        ;;
    -e | --extension)
        show_extension="true"
        shift
        ;;
    -l | --listing)
        show_listing="true"
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

# Check if the file exists
if [[ ! -f "$file_path" ]]; then
    echo "File not found: $file_path"
    exit 1
fi

# Call the filter_file_details function to display filtered file details
filter_file_details "$file_path" "$size_filter" "$date_filter" "$owner_filter" "$show_extension" "$show_listing"
