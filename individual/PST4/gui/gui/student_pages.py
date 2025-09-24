# gui/student_pages.py
import streamlit as st

def show_student_management_page(manager):
    """Renders all components for the student management page."""
    st.header("Student Management")

    # --- Search Section (remains the same) ---
    st.subheader("Find a Student")
    # ...
    with st.form("find_student_form"):
        student_id = st.number_input("Student ID", step=1, min_value=1)
        submitted = st.form_submit_button("Show student details")

        if submitted:
            if student_id:
                student = manager.find_student_by_id(student_id)
                if student:
                    table_data = [
                        ["ID","Name","Enrolled courses"],
                        [student.get_user_id(),student.get_user_name(),student.get_enrolled_course_ids()]
                    ]

                    st.table(table_data)

    # --- Registration Section (now works correctly) ---
    st.subheader("Register New Student")
    with st.form("registration_form"):
        reg_name = st.text_input("New Student Name")
        reg_instrument = st.text_input("First Instrument")
        submitted = st.form_submit_button("Register Student")
        
        if submitted:
            # This call now works because we implemented the method in PST3.
            # TODO: Add a check for blank name/instrument.
            if reg_name and reg_instrument:
                new_student = manager.register_new_student(reg_name, reg_instrument)
                if new_student:
                    st.success(f"Successfully registered {reg_name}!")
                    # You can use st.balloons() for extra flair.
                else:
                    st.error(f"Could not register student. A teacher for {reg_instrument} might not be available.")
            else:
                st.warning("Please enter both a name and an instrument.")

    st.subheader("Replace course")
    with st.form("replace_course_form"):
        student_id = st.number_input("Student ID",step=1, min_value=1)
        from_course_id = st.number_input("From course (ID)",step=1, min_value=100)
        to_course_id = st.number_input("To course (ID)",step=1, min_value=100)
        submitted = st.form_submit_button("Replace course")

        if submitted:
            if student_id and from_course_id and to_course_id:
                course_replacement = manager.replace_course(student_id,from_course_id,to_course_id)
                if course_replacement:
                    st.success(f"Successfully replaced {from_course_id} with {to_course_id}.")
                else:
                    st.error("Could not find either/all-of student ID,from course ID or to course ID.")
            else:
                st.warning("Please enter in all 3 fields.")

