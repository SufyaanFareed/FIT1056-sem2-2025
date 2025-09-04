import json
import datetime
from app.app.student import StudentUser
from app.app.teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        # TODO: Initialize the new attendance_log attribute as an empty list.
        self.attendance_log = []
        # ... (next_id counters) ...
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # TODO: Load students, teachers, and courses as before.
                # ...
                #Loop through the "students" list 
                for this_student in data.get("students",[]): 
                    #Instantiate each student using the StudentUser sub-class and append the student to the self.students list   
                    self.students.append(StudentUser(this_student["id"],this_student["name"],this_student["enrolled_course_ids"])) 
                
                for this_teacher in data.get("teachers",[]):
                    self.teachers.append(TeacherUser(this_teacher["id"],this_teacher["name"],this_teacher["speciality"]))
                
                for this_course in data.get("courses",[]):
                    self.courses.append(Course(this_course["id"],this_course["name"],this_course["instrument"],this_course["teacher_id"],this_course["enrolled_student_ids"],this_course["lessons"]))         
                # TODO: Correctly load the attendance log.
                # Use .get() with a default empty list to prevent errors if the key doesn't exist.
                self.attendance_log = data.get("attendance", [])
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # TODO: Create a 'data_to_save' dictionary.
        data_to_save = {
            #Create a dictionary for each object's attributes in self.students list
            #each dictionary is then added to a list which is the value for the key ""students"
            "students": [s.__dict__ for s in self.students],
            "teachers": [t.__dict__ for t in self.teachers],
            "courses": [c.__dict__ for c in self.courses],
            # TODO: Add the attendance_log to the dictionary to be saved.
            # Since it's already a list of dicts, no conversion is needed.
            "attendance": self.attendance_log,
            # ... (next_id counters) ...
        }
        # TODO: Write 'data_to_save' to the JSON file.
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def check_in(self, student_id, course_id):
        """Records a student's attendance for a course after validation."""
        # This implementation remains the same, but it will now function correctly.
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        
        if not student or not course:
            print("Error: Check-in failed. Invalid Student or Course ID.")
            return False
            
        timestamp = datetime.datetime.now().isoformat()
        check_in_record = {"student_id": student_id, "course_id": course_id, "timestamp": timestamp}
        
        # This line will now work without causing an AttributeError.
        self.attendance_log.append(check_in_record)
        self._save_data() # This will now correctly save the attendance log.
        print(f"Success: Student {student.name} checked into {course.name}.")
        return True

    # TODO: Also implement find_student_by_id and find_course_by_id helper methods.

    def find_student_by_id(self,this_id):
        for student in self.students:
            if student.get_user_id()==this_id:
                return student

    def find_course_by_id(self,this_id):
        for course in self.courses:
            if course.get_course_id()==this_id:
                return course
            
    def lessons_for_the_day(self,day):
        days_lessons=[]
        for course in self.courses:
            for lesson in course.get_lessons_list():
                if lesson["day"]==day:
                    days_lessons.append(lesson)
        return days_lessons

    def replace_course(self,student_id,from_course_id,to_course_id):
        #Ensure that the student of mentioned student_id exists 
        if self.find_student_by_id(student_id):
            #Ensure that that from_course_id and to_course_id exist
            if self.find_course_by_id(from_course_id) and self.find_course_by_id(to_course_id):
                #store the returned student object in this_student
                this_student=self.find_student_by_id(student_id)
                #Loop through this_student's enrolled courses list until a match is found
                for course_index in range(len(this_student.get_enrolled_course_ids())):
                    if (this_student.get_enrolled_course_ids())[course_index] == from_course_id:
                        #replace this course (from_course_id) with the new course (to_course_id) and exit loop
                        (this_student.get_enrolled_course_ids())[course_index]=to_course_id
                        break
                
                #store the returned course object in this_course
                this_course=self.find_course_by_id(from_course_id)
                #Loop through this_course's enrolled students list until a match is found
                for course_index in range(len(this_course.get_enrolled_student_ids())):
                    if (this_course.get_enrolled_student_ids())[course_index] == student_id:
                        #Unenrol the student from this course
                        (this_course.get_enrolled_student_ids()).pop(course_index)
                        break
                
                #store the returned course object in this_course
                this_course=self.find_course_by_id(to_course_id)
                #Enrol the student in this course
                (this_course.get_enrolled_student_ids()).append(student_id)

                self._save_data()



        

                