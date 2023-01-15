import json

def f(age, course, average):
    with open('test.json', 'r') as f:
        data = json.load(f)
    
    student_amount = 0
    
    for student in data:
        
        if student['age'] >= age:
            
            if 'studies' in student:
                
                for student_course in student['studies']['courses']:
                    
                    if student_course['name'] == course:
                        
                        grade_sum = sum(student_course['grades'])
                        grade_amount = len(student_course['grades'])
                        grade_average = grade_sum/grade_amount
                        
                        if grade_average >= average:
                            student_amount += 1
    
    return student_amount
            
        
        
print(f(21, "statistics", 4))