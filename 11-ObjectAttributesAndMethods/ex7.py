class Student():

    university = "UEK Kraków"
    id =  1000
    

    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname = surname
        self.field_of_study = field_of_study
        self.id = Student.id
        Student.id += 1

    def __str__(self):
        return self.name + " " + self.surname + " " + str(self.id) + ", " + self.field_of_study + ", " + self.university


student1 = Student("aaaa", "aaaa", "aaaa")
student2 = Student("aaaa", "aaaa", "aaaa")
print(student1)
print(student2)