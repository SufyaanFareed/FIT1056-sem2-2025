# main.py - The View Layer
from app.app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    # Notice: This code does not need to change. It doesn't care where the Course class lives.
    # It only talks to the manager.
    # TODO: Call a method on the manager to get the day's lessons and print them.
    for lesson in manager.lessons_for_the_day(day):
        print("Lesson ID: " + str(lesson["lesson_id"]))
        print("Day: " + lesson["day"])
        print("Start Time: " + lesson["start_time"])
        print("room: " + lesson["room"])
        print()

def switch_course(manager, student_id, from_course_id, to_course_id):
    # TODO: Implement the logic to switch a student by calling methods on the manager.
    manager.replace_course(student_id,from_course_id,to_course_id)
    print(f"Student ID:{student_id} has been unenrolled from {from_course_id} and enrolled in {to_course_id}.")

def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        # TODO: Create a menu for the new PST3 functions.
        print("1. Display today's lessons")
        print("2. Switch student's courses")
        print("3. Record student attendance")
        print("q. Exit program")
        # Get user input and call the appropriate view function, passing 'manager' to it.
        print()
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
        elif choice == "2":
            student_ID=int(input("Enter student ID: "))
            from_course_ID=int(input("Enter course ID to unenrol from: "))
            to_course_ID=int(input("Enter course ID to enrol in: "))
            switch_course(manager,student_ID, from_course_ID, to_course_ID)
            print()
        elif choice == "3":
            student_ID=int(input("Enter student ID: "))
            course_ID=int(input("Enter course ID to record attendance for: "))
            manager.check_in(student_ID,course_ID)
        elif choice.lower() == 'q':
            break
        
if __name__ == "__main__":
    main()