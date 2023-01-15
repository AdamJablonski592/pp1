import json

new_arr = []
with open('students.json', 'r') as f:
    data = json.load(f)
    i = 0
    while i < len(data):
        data_row = data[i]
        students = {
            "name": data_row["name"],
            "surname": data_row["surname"],
            "student_ID": data_row["student_ID"]
        }
        new_arr.append(students)
        i += 1

with open('limited.json', 'w') as f:
    json.dump(new_arr, f, indent=4)