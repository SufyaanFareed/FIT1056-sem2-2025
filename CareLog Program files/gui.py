import streamlit as st
from brain import SystemManager
from user_base_class import user
from patient_class import patient
from admin_class import admin
from nurse_class import nurse
from doctor_class import doctor

# Initializing the session states
if 'manager' not in st.session_state:
    st.session_state.manager = SystemManager()
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None
if 'user_type' not in st.session_state:
    st.session_state.user_type = None

def main():
    st.title("CareLog Healthcare Management System")
    
    # Check if user is logged in
    if st.session_state.logged_in_user is None:
        #This step ensures that memory is always synchronised with the database when the streamlit GUI is running
        #Previously, when a user would log out and be returned to the login page,
        #data would be saved to the JSON files but memory would not be updated to reflect this
        st.session_state.manager = SystemManager()
        show_login_page()
    else:
        show_dashboard()

def show_login_page():
    st.header("Welcome to CareLog Management System")
    
    # Simple choice between login and create account
    choice = st.radio("Select an option:", ["Login", "Create Account"])
    
    if choice == "Login":
        login_form()
    else:
        registration_form()

#Function for background image
#Image is fetched from a URL
def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://as1.ftcdn.net/jpg/01/98/81/40/1000_F_198814073_1Ou5wprYWhldGzS6AWzPuSvx4L9E2TEt.jpg");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: local; /* or fixed */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

def login_form():
    st.subheader("Login")
    
    user_id = st.number_input("Enter User ID:", min_value=1, step=1)
    password = st.text_input("Enter Password:", type="password")
    
    user_role = st.selectbox("Select Your Role:", ["Doctor", "Nurse", "Admin", "Patient"])
    
    if st.button("Login"):
        # Choose the correct list based on role
        if user_role == "Doctor":
            user_list = st.session_state.manager.doctors
        elif user_role == "Nurse":
            user_list = st.session_state.manager.nurses
        elif user_role == "Admin":
            user_list = st.session_state.manager.admins
        else:
            user_list = st.session_state.manager.patients
        
        # Try to login and return the logged in user object if login is succesful so that methods can be called on it
        logged_in_user = st.session_state.manager.log_in(user_id, password, user_list)
        
        if logged_in_user:
            st.session_state.logged_in_user = logged_in_user
            st.session_state.user_type = user_role
            st.success("Login successful!")
            #Rerun the script from the beginning now taking into account that the user is logged in
            st.rerun()
        else:
            st.error("Invalid ID, password, or role.")

def registration_form():
    st.subheader("Create New Account")
    
    full_name = st.text_input("Enter Full Name:")
    user_type = st.selectbox("Select User Type:", ["Doctor", "Nurse", "Admin", "Patient"])
    password1 = st.text_input("Enter Password:", type="password", key="pass1")
    password2 = st.text_input("Confirm Password:", type="password", key="pass2")
    
    if st.button("Create Account"):
        if password1 != password2:
            st.error("Passwords do not match!")
        elif not full_name:
            st.error("Please enter your name")
        else:
            # Choose the correct list
            if user_type == "Doctor":
                user_list = st.session_state.manager.doctors
            elif user_type == "Nurse":
                user_list = st.session_state.manager.nurses
            elif user_type == "Admin":
                user_list = st.session_state.manager.admins
            else:
                user_list = st.session_state.manager.patients
            
            # Create account
            new_user, user_id = st.session_state.manager.add_user(full_name, password1, user_list)
            
            if new_user:
                st.success("Your Account has been created successfully!")
                st.info(f"Your User ID is: {user_id}")
                st.info("Please remember this ID for login")
                #log_out() is called to save the new user to the JSON file
                st.session_state.manager.log_out()

def show_dashboard():
    user = st.session_state.logged_in_user
    user_type = st.session_state.user_type
    
    st.title(f"Welcome {user.name}!")
    st.write(f"User ID: {user.user_id}")
    st.write(f"Role: {user_type}")
    
    if st.button("Logout"):
        st.session_state.manager.log_out()
        st.session_state.logged_in_user = None
        st.session_state.user_type = None
        st.success("Logged out successfully!")
        #Return the user to the login page 
        st.rerun()

    if st.button("Help"):
        st.write("Link to the user documentation is https://drive.google.com/file/d/1M4mumciNVzBUW9VkGI-Zc-uKE-pE952c/view?usp=sharing")
                 
    st.write("---")
    
    # Show different options based on user type
    if isinstance(user, doctor):
        show_doctor_page(user)
    elif isinstance(user, nurse):
        show_nurse_page(user)
    elif isinstance(user, admin):
        show_admin_page(user)
    elif isinstance(user, patient):
        show_patient_page(user)

def show_doctor_page(user):
    st.header("Doctor Dashboard")

    #If the doctor has any assigned patients then proceed
    if len(user.assigned_patients)>0:
        #Initialise the doctor's patient_logs dictionary (see the doctor class for more detailed info)
        user.fetch_patient_logs(st.session_state.manager.nurses)

        option = st.selectbox("Select an option:", 
                            ["Record clinical observation", 
                            "Edit patient log", 
                            "Generate patient summary report", 
                            "Delete patient log"])
        
        assigned_patients_list = user.show_assigned_patients(st.session_state.manager.patients)
        #This block displays assigned patients in a table
        if len(assigned_patients_list)>0:
            table_data = [
                ["Patient ID","Name"]
            ]

            for this_patient in assigned_patients_list:
                row = []
                row.append(this_patient.user_id)
                row.append(this_patient.name)
                table_data.append(row)
            
            st.write("Assigned Patients:")
            st.table(table_data)
        else:
            st.write("You have not been assigned any patients")

        patient_id = st.selectbox("Patient ID", [this_patient.user_id for this_patient in assigned_patients_list])

        patient_logs = user.get_patient_log_history(patient_id)
        #This block displays,in a tabular format, the patient logs of the selected patient_id if there are any
        if patient_logs:
            if len(patient_logs)>0:
                table_data = [
                    ["Log history"]
                ]

                for this_log in patient_logs:
                    table_data.append([this_log])

                st.table(table_data)
            else:
                st.write("No patient logs to display")
        else:
            st.write("No patient logs to display.")
        
        if option == "Record clinical observation":
            #patient_id = st.selectbox("Patient ID", [this_patient.user_id for this_patient in assigned_patients_list])
            observation = st.text_area("Enter observation:")
            
            if st.button("Record"):
                message = user.record_clinical_observation(patient_id, observation)
                st.write(message)
        
        elif option == "Edit patient log":
            log_index = st.number_input("Log number:", min_value=0, step=1)
            new_entry = st.text_area("Enter new details:")
            
            if st.button("Edit"):
                message = user.edit_patient_log(patient_id, log_index, new_entry)
                st.write(message)
        
        elif option == "Generate patient summary report":
            #patient_id = st.selectbox("Patient ID", [this_patient.user_id for this_patient in assigned_patients_list])
            
            if st.button("Generate Report"):
                message = user.generate_patient_summary_report(patient_id)
                st.text_area("Report:", message, height=200)
        
        elif option == "Delete patient log":
            #patient_id = st.selectbox("Patient ID", [this_patient.user_id for this_patient in assigned_patients_list])
            log_index = st.number_input("Log number:", min_value=0, step=1)
            
            if st.button("Delete"):
                message = user.delete_patient_log(patient_id, log_index)
                st.write(message)
    else:
        st.write("You have not been assigned any patients")

def show_nurse_page(user):
    st.header("Nurse Dashboard")
    
    #The nurse page is similar to the doctors page
    option = st.selectbox("Select an option:", 
                          ["Record clinical observation", 
                           "Edit patient log", 
                           "Generate patient summary report", 
                           "Delete patient log"])
    
    assigned_patients_list = user.show_assigned_patients(st.session_state.manager.patients)
    #Display assigned patients if there are any in a table format
    if len(assigned_patients_list)>0:
        table_data = [
            ["Patient ID","Name"]
        ]

        for this_patient in assigned_patients_list:
            row = []
            row.append(this_patient.user_id)
            row.append(this_patient.name)
            table_data.append(row)
        
        st.write("Assigned Patients:")
        st.table(table_data)
    else:
        st.write("You have not been assigned any patients")

    patient_id = st.selectbox("Patient ID", [this_patient.user_id for this_patient in assigned_patients_list])

    patient_logs = user.get_patient_log_history(patient_id)

    #Display patient_logs of selected patient_id (if there are any)
    if patient_logs:
        if len(patient_logs)>0:
            table_data = [
                ["Log history"]
            ]

            for this_log in patient_logs:
                table_data.append([this_log])

            st.table(table_data)
        else:
            st.write("No patient logs to display")
    
    if option == "Record clinical observation":
        #patient_id = st.selectbox("Patient ID", [this_patient.user_id for this_patient in assigned_patients_list])
        observation = st.text_area("Enter observation:")
        
        if st.button("Record"):
            message = user.record_clinical_observation(patient_id, observation)
            st.write(message)
    
    elif option == "Edit patient log":
        log_index = st.number_input("Log number:", min_value=0, step=1)
        new_entry = st.text_area("Enter new details:")
        
        if st.button("Edit"):
            message = user.edit_patient_log(patient_id, log_index, new_entry)
            st.write(message)
    
    elif option == "Generate patient summary report":
        if st.button("Generate Report"):
            message = user.generate_patient_summary_report(patient_id)
            st.text_area("Report:", message, height=200)
    
    elif option == "Delete patient log":
        log_index = st.number_input("Log number:", min_value=0, step=1)
        
        if st.button("Delete"):
            message = user.delete_patient_log(patient_id, log_index)
            st.write(message)

def show_admin_page(user):
    st.header("Admin Dashboard")
    
    option = st.selectbox("Select an option:", ["See all new patients", "Assign staff to patients"])
    
    if option == "See all new patients":
        st.subheader("New Patients")
        if st.session_state.manager.patients_without_doctors:
            for patient in st.session_state.manager.patients_without_doctors:
                st.write(f"Name: {patient.name}, ID: {patient.user_id}")
        else:
            st.write("No new patients")
    
    elif option == "Assign staff to patients":
        if st.button("Assign Staff"):
            message = user.assign_staff_to_patient(
                st.session_state.manager.nurses,
                st.session_state.manager.doctors,
                st.session_state.manager.patients_without_doctors
            )
            st.write(message)

def show_patient_page(user):
    st.header("Patient Dashboard")
    
    option = st.selectbox("Select an option:", ["Set my preferences", "See my preferences"])
    
    if option == "Set my preferences":
        st.subheader("Set Preferences")
        
        #List of days from which patient can choose from
        days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day1 = st.selectbox("Preferred visiting day 1:", days_list)

        #Remove the already chosen day so they cannot choose it again
        days_list.pop(days_list.index(day1))
        day2 = st.selectbox("Preferred visiting day 2:", days_list)

        #Again, remove the already chosen days...
        days_list.pop(days_list.index(day2))
        day3 = st.selectbox("Preferred visiting day 3:", days_list)
        
        visiting_days = []
        visiting_days.append(day1)
        visiting_days.append(day2)
        visiting_days.append(day3)
        
        #Only 2 possible visiting hours from which they can choose
        visiting_hours = st.selectbox("Preferred visiting hours:", ["14:00 - 15:00","19:00 - 20:00"])
        language = st.text_input("Preferred language:")
        
        if st.button("Save Preferences"):
            user.set_preferences(visiting_days, visiting_hours, language, st.session_state.manager.patient_preferences)
            st.success("Preferences saved!")
    
    elif option == "See my preferences":
        st.subheader("My Preferences")
        
        # Get preferences from dictionary
        if str(user.user_id) in st.session_state.manager.patient_preferences:
            prefs = st.session_state.manager.patient_preferences[str(user.user_id)]
            st.write(f"Name: {user.name}")
            st.write(f"Preferred Visiting Days: {', '.join(prefs['preferred_visiting_days'])}")
            st.write(f"Preferred Visiting Hours: {prefs['preferred_visiting_hours']}")
            st.write(f"Language: {prefs['language']}")
        else:
            st.write("You have not entered any preferences")

if __name__ == "__main__":

    main()

