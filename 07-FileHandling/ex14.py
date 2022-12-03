file_name = input("File name: ")
with open(file_name, 'r') as f:
    x = len(f.readlines())
    print(f"Number of lines: {x}")