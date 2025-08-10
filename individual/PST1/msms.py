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

def add_teacher(name, speciality):
    global next_teacher_id
    new_teacher = Teacher(next_teacher_id, name, speciality)
    teacher_db.append(new_teacher)
    next_teacher_id += 1
    print(f"Core: Teacher '{name}' added successfully.")

def list_students():
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system.")
        return
    for student in student_db:
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {student.enrolled_in}")

def list_teachers():
    print("\n--- Teacher List ---")
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")

def find_students(term):
    print(f"\n--- Finding Students matching '{term}' ---")
    matchingStudents=[]
    for student in student_db:
        if student.name==term:
            matchingStudents.append(student)
    if not matchingStudents:
        print("No match found.")
    else:
        for student in matchingStudents:
            print(f"studentID:{student.id} name:{student.name}")

def find_teachers(term):
    print(f"\n--- Finding Teachers/specialities matching '{term}' ---")
    matchingTerm=[]
    for teacher in teacher_db:
        if teacher.name==term or teacher.speciality==term:
            matchingTerm.append(teacher)
    if not matchingTerm:
        print("No match found.")
    else:
        for teacher in matchingTerm:
            print(f"teacherID:{teacher.id} name:{teacher.name} speciality:{teacher.speciality}")

def find_student_by_id(student_id):
    for student in student_db:
        if student.id == student_id:
            return student
    return None

def front_desk_register(name, instrument):
    global next_student_id
    new_student = Student(next_student_id, name)
    student_db.append(new_student)
    next_student_id += 1
    
    front_desk_enrol(new_student.id, instrument)
    print(f"Front Desk: Successfully registered '{name}' and enrolled them in '{instrument}'.")

def front_desk_enrol(student_id, instrument):
    student = find_student_by_id(student_id)
    if student:
        student.enrolled_in.append(instrument)
        print(f"Front Desk: Enrolled student {student_id} in '{instrument}'.")
    else:
        print(f"Error: Student ID {student_id} not found.")

def front_desk_lookup(term):
    print(f"\n--- Performing lookup for '{term}' ---")
    find_students(term)
    find_teachers(term)         

def main():
    add_teacher("Dr. Keys", "Piano")
    add_teacher("Ms. Fret", "Guitar")

    while True:
        print("\n===== Music School Front Desk =====")
        print("1. Register New Student")
        print("2. Enrol Existing Student")
        print("3. Lookup Student or Teacher")
        print("4. (Admin) List all Students")
        print("5. (Admin) List all Teachers")
        print("q. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            instrument = input("Enter instrument to enrol in: ")
            front_desk_register(name, instrument)
        elif choice == '2':
            try:
                student_id = int(input("Enter student ID: "))
                instrument = input("Enter instrument to enrol in: ")
                front_desk_enrol(student_id, instrument)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '3':
            term = input("Enter search term: ")
            front_desk_lookup(term)
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_teachers()
        elif choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()