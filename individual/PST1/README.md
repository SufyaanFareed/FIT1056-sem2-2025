Copy and paste the following to test fragment1:

#CODE FOR TESTING Fragment1:
#--------------------
for count in range(2):
    inputName=input("Please enter student name: ")
    #Create an instance of the Student class
    thisStudent=Student(next_student_id,inputName)
    #Append the student to the student_db list
    student_db.append(thisStudent)
    #Increment next_student_id for the next available ID to be used by the next student
    next_student_id+=1

print()
#Display all students in the database 
for count in range(2):
    print(f"name:{student_db[count].name}  studentID:{student_db[count].id}")
#A similar approach can be used to test the Teacher class
#--------------------