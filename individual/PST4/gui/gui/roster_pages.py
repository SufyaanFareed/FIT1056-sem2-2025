# gui/roster_pages.py
import streamlit as st
import pandas as pd

def show_roster_page(manager):
    """Renders the daily roster and check-in functionality."""
    st.header("Daily Roster")

    # --- View Roster Section (remains the same) ---
    with st.form("daily_roster_form"):
        day = st.selectbox("Select a day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    # ... (code to display the dataframe) ...
        submitted=st.form_submit_button("Show roster")
        
        if submitted:
            lessons_list=manager.lessons_for_the_day(day)
            if len(lessons_list)>0:
                table_data=[
                    ["Lesson ID","Day","Start time","Room"]
                ]
                for lesson in manager.lessons_for_the_day(day):
                    lesson_details=[]
                    lesson_details.append(lesson["lesson_id"])
                    lesson_details.append(lesson["day"])
                    lesson_details.append(lesson["start_time"])
                    lesson_details.append(lesson["room"])
                    table_data.append(lesson_details)
                st.table(table_data)
            else:
                st.write("No Lessons on this day")
    
    # --- Student Check-in Section (now works correctly) ---
    st.subheader("Student Check-in")
    with st.form("check_in_form"):
        # To make this user-friendly, we should populate the dropdowns dynamically.
        # Get lists of student names and course names from the manager.
        student_list = {s.name: s.id for s in manager.students}
        course_list = {c.name: c.id for c in manager.courses}
        
        selected_student_name = st.selectbox("Select Student", student_list.keys())
        selected_course_name = st.selectbox("Select Course", course_list.keys())
        
        submitted = st.form_submit_button("Check-in Student")

        if submitted:
            # Convert the selected names back to IDs
            student_id = student_list[selected_student_name]
            course_id = course_list[selected_course_name]

            # This call now works because we implemented the method in PST3.
            success = manager.check_in(student_id, course_id)

            if success:
                st.success(f"Checked in {selected_student_name} for {selected_course_name}!")
            else:
                # The manager's print statements will go to the console, but we can add a GUI error too.
                st.error("Check-in failed. See console for details. (Is the student enrolled in that course?)")