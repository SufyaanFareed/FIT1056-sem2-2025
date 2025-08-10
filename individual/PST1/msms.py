class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.enrolled_in = []

class Teacher:
    def __init__(self, teacher_id, name, speciality):
        self.id = teacher_id
        self.name = name
        self.speciality = speciality

student_db = []
teacher_db = []
next_student_id = 1
next_teacher_id = 1

#CODE FOR TESTING Fragment1:
#--------------------
for count in range(2):
    studentName=input("Please enter student name: ")
#     #Create an instance of the Student class
    thisStudent=Student(next_student_id,studentName)
#     #Append the student to the student_db list
    student_db.append(thisStudent)
#     #Increment next_student_id for the next available ID to be used by the next student
    next_student_id+=1

print()
#Display all students in the database 
for count in range(2):
    print(f"name:{student_db[count].name}  studentID:{student_db[count].id}")
#A similar approach can be used to test the Teacher class
#--------------------