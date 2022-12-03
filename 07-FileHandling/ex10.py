name = input("Name: ")
surname = input("Surname: ")
university = input("University: ")
field_of_study = input("Field of study: ")

with open('data.txt', 'w') as f:
    lines = [name, "\n", surname, "\n", university, "\n", field_of_study]
    f.writelines(lines)
    f.close()