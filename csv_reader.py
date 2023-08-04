


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
        print("Usage: python3 csv_reader.py filename -t num_columns -c1 header1 -c2 header2 ...")
        sys.exit(1) 
    
    filename = sys.argv[1]  
    
  
    t_flag_index = sys.argv.index('-t')
    num_columns = int(sys.argv[t_flag_index + 1]) 
    flags, custom_columns = parse_flags(sys.argv[t_flag_index + 2:], num_columns)  
    
    lines = read_file(filename)  
    headers = lines[0].strip().split(',') 
    
    if not 1 <= num_columns <= len(headers):
        print(f"Error: Invalid input flag value.")
        sys.exit(1)  
    
    if flags['-t']:
        if num_columns != len(headers):
            print(f"Error: Number of columns provided does not match the actual number of columns in the file.")
            sys.exit(1)  
    col_widths = []
    for col_num, header in custom_columns.items():
        max_word_count = max(len(values[col_num - 1].split()) for values in lines[1:])
        col_widths.append(max(max_word_count + 10, len(header) + 10))

 
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

    for line in lines[0:]:
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
