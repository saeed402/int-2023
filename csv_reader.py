

# Function to read the contents of a file and return them as a list of lines
    # Try to open the file and read its lines
    # If the file is not found, print an error message and exit the program

# Function to parse command-line flags and custom column information

    
    # Loop through command-line arguments to parse flags and custom column info
    # Update the 'flags' and 'custom_columns' dictionaries accordingly


# Main function that processes the input and generates the formatted table
# Check if the correct number of command-line arguments is provided
# If not, print a usage message and exit the program
    

# Get the input filename from command-line arguments
# Find the index of the '-t' flag to determine the starting point for custom column info
    
# Define a dictionary to store custom column information
    
# Read the contents of the input file into 'lines' list
# Split the header line to extract the column headers

# Check if the specified number of columns is valid
# If not, print an error message and exit the program
    
# Check if '-t' flag is used with custom columns
# If so, verify if the number of columns matches the header
# If not, print an error message and exit the program
    
# Create a list to store calculated column widths
# Loop through custom columns and calculate their widths
# Based on the maximum word count in the column data and header length 
# Print header line using calculated column widths
# Print header row with centered column headers using calculated padding    
# Print separator line for the header 
# Loop through data lines and print formatted rows
# Center-align values in each column using calculated padding
#print separator line for the footer
# Check if the program is being run as the main module
#if _name_ == "_main_":
# Call the main function to start program execution
    


import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def parse_flags(args, num_columns):
    flags = {
        '-t': False,
    }
    custom_columns = {}
    
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == '-t':
            flags[arg] = True
            i += 1
        elif arg.startswith('-c'):
            parts = arg.split('=')
            if len(parts) == 2:
                column_num = int(parts[0][2:])
                header_val = parts[1]
                if 1 <= column_num <= num_columns:
                    custom_columns[column_num] = header_val
                else:
                    print(f"Error: Invalid flag value")
                    sys.exit(1)
                i += 1
            else:
                print(f"Error: Invalid flag '{arg}'.")
                sys.exit(1)
        else:
            print(f"Error: Invalid flag '{arg}'.")
            sys.exit(1)
    
    return flags, custom_columns

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 table_task.py filename -t num_columns -c1 header1 -c2 header2 ...")
        sys.exit(1)

    filename = sys.argv[1]

    t_flag_index = sys.argv.index('-t')
    num_columns = int(sys.argv[t_flag_index + 1])
    
    # Define custom_columns dictionary to hold column information
    custom_columns = parse_flags(sys.argv[t_flag_index + 2:], num_columns)[1]

    lines = read_file(filename)
    headers = lines[0].strip().split(',')

    if not 1 <= num_columns <= len(headers):
        print(f"Error: Invalid input flag value.")
        sys.exit(1)

    if '-t' in custom_columns:
        if num_columns != len(headers):
            print(f"Error: Number of columns provided does not match the actual number of columns in the file.")
            sys.exit(1)

    col_widths = []

    for col_num, header in custom_columns.items():
        max_word_count = max(len(values[col_num - 1].split()) for values in lines[1:])
        if col_num == 5:  # Check for column 5
            min_col_width = len(header) + 60  # Increased width for column 5
        else:
            min_col_width = len(header) + 25  # Minimum width for other columns
        col_widths.append(max(max_word_count + 20, min_col_width))  # Increase padding

    header_line = "="
    for col_width in col_widths:
        header_line += "=" * (col_width + 2) + "="
    print(header_line)

    header_line = "|"
    for header, col_width in zip(custom_columns.values(), col_widths):
        padding = (col_width - len(header)) // 2
        header_line += " {}{}{} |".format(" " * padding, header, " " * (col_width - len(header) - padding))
    print(header_line)

    header_line = "="
    for col_width in col_widths:
        header_line += "=" * (col_width + 2) + "="
    print(header_line)

    for line in lines[1:]:  # Skip the header row
        values = line.strip().split(',')
        row = "|"
        for col_num, col_width in zip(custom_columns.keys(), col_widths):
            if col_num <= len(values):
                value = values[col_num - 1]
            else:
                value = ""
            padding = (col_width - len(value)) // 2
            row += " {}{}{} |".format(" " * padding, value, " " * (col_width - len(value) - padding))
        print(row)

    footer_line = "-"
    for col_width in col_widths:
        footer_line += "-" * (col_width + 2) + "-"
    print(footer_line)

if __name__ == "__main__":
    main()
