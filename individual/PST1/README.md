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

Copy and paste the following after having merged fragment1 and fragment2:

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

Copy and paste the following code after having merged fragments 1,2 and 3 together:

#CODE FOR TESTING Fragment3:
#---------------------
front_desk_register("sufyaan","piano")
front_desk_register("zakaria","guitar")
front_desk_register("Layla","drums")

#Testing all possible paths of the 'if...' statement in the front_desk_enrol procedure
front_desk_enrol(2,"flute")
front_desk_enrol(7,"trumpet")

#Testing all possible return options of the function find_student_by_id
find_student_by_id(9)
find_student_by_id(3)


front_desk_lookup("zakaria")
front_desk_lookup("francois")
#---------------------