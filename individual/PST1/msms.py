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

# --- Core Helper Functions ---
def add_teacher(name, speciality):
    global next_teacher_id
    # TODO: Create a new Teacher object using the next available ID.
    new_teacher = Teacher(next_teacher_id, name, speciality)
    # TODO: Append the new_teacher to the teacher_db list.
    teacher_db.append(new_teacher)
    # TODO: Increment the next_teacher_id counter.
    next_teacher_id += 1
    print(f"Core: Teacher '{name}' added successfully.")

def list_students():
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system.")
        return
    # TODO: Loop through student_db. For each student, print their ID, name, and their enrolled_in list.
    for student in student_db:
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {student.enrolled_in}")

def list_teachers():
    # TODO: Implement the logic to list all teachers, similar to list_students().
    print("\n--- Teacher List ---")
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")

def find_students(term):
    print(f"\n--- Finding Students matching '{term}' ---")
    # TODO: Create an empty list to store results.
    listOfMatches=[]
    # Loop through student_db. If the search 'term' (case-insensitive) is in the student's name,
    # add them to your results list.
    for student in student_db:
        if student.name.lower().find(term.lower())!=-1:
            listOfMatches.append(student)
    # After the loop, if the results list is empty, print "No match found."
    # Otherwise, print the details for each student in the results list.
    if not listOfMatches:
        print(f"No matches were found for {term}.")
    else:
        for student in listOfMatches:
            print(f"student name:{student.name}  student ID:{student.id}")


def find_teachers(term):
    # TODO: Implement this function similar to find_students, but check
    # for the term in BOTH the teacher's name AND their speciality.
    print(f"\n--- Finding teachers matching '{term} ---'")
    listOfMatches=[]
    for teacher in teacher_db:
        if (teacher.name.lower().find(term.lower())!=-1) or (teacher.speciality.lower().find(term.lower())!=-1):
            listOfMatches.append(teacher)

    if not listOfMatches:
        print(f"No matches were found for {term}.")
    else:
        for teacher in listOfMatches:
            print(f"teacher name:{teacher.name}  teacher ID:{teacher.id}   speciality:{teacher.speciality}")

#CODE FOR TESTING Fragment2:
#--------------------
add_teacher("Jeremiah","Piano")
add_teacher("Kulsum","Guitar")

for count in range(2):
    studentName=input("Please enter student name: ")
    #Create an instance of the Student class
    thisStudent=Student(next_student_id,studentName)
    #Append the student to the student_db list
    student_db.append(thisStudent)
    #Increment next_student_id for the next available ID to be used by the next student
    next_student_id+=1

#Testing whether the find_students function can return a student whose name has a matching substring as 'term'
#The input name for one of the students should have yaan as a substring
find_students("yaan")
#Testing whether or not find_teachers is case-sensitive
#find_teachers should return Jeremiah, disregarding the fact that his speciality is 'Piano' and not 'PIANO'
find_teachers("PIANO")
print()

list_teachers()
list_students()
#--------------------