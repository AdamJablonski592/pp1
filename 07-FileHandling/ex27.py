import re

with open('grades.txt', 'r') as f:
    f_content = f.read()
    grades = re.findall("\d+\.\d+", f_content)
    sum = 0
    amount = 0
    for item in grades:
        sum += float(item)
        amount += 1
        
    result = sum / amount
    print(round(result, 2))
        
    