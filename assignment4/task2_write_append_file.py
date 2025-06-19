# task2_write_append_file.py

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data + '\n')

def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_file(filename):
    print("\nFinal content of output.txt:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Main execution
if __name__ == "__main__":
    user_input = input("Enter text to write to the file: ")
    print("Data successfully wirtten to output.txt.")
    write_to_file("output.txt", user_input)

    additional_data = input("Enter additional text to append: ")
    print("Data successfully appended.")
    append_to_file("output.txt", additional_data)

    read_file("output.txt")