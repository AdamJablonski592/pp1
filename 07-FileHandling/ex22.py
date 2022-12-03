import csv
with open('students.txt', 'r') as f:
    f_reader = csv.reader(f, delimiter=',')
    array = []
    for line in f_reader:
        array.append(line)
        
    for item in array[1:]:
        if int(item[2]) < 30:
            print(item[0], " " * (8 - len(item[0])), item[1], " " * (9 - len(item[1])), item[4])
        else:
            continue