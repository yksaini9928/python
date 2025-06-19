
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File contents:\n")
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Main execution
if __name__ == "__main__":
    read_file("sample.txt")