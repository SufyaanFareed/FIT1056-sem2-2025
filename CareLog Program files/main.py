from brain import SystemManager
from user_base_class import doctor
from patient_class import patient
from admin_class import admin
from nurse_class import nurse

def main():
    #Create an instance of the systemManager class
    manager=SystemManager()

    print("SELECT OPTION:")
    print("1. Create an account")
    print("2. Log in")

    option=input("Enter option: ")
    print()

    #Do the following if the user selects option 1
    if option=="1":
        print("SELECT USER TYPE:")
        print("1. Doctor")
        print("2. Nurse")
        print("3. Admin")
        print("4. Patient")

        option=input("option: ")
        print()

        entered_name=input("Enter your full name: ")
        verification1=input("Enter password: ")
        verification2=input("Confirm password: ")

        #Data verification so that user makes no mistakes when entering their password
        if verification1==verification2:
            entered_password=verification2
        else:
            print("passwords do not match")

        #Check if data verification was successful by checking if entered_password is True
        if entered_password:
            #Add the user to the correct object list (doctors, nurses etc) depending on the option they chose
            if option=="1":
                this_user, user_id=manager.add_user(entered_name,entered_password,manager.doctors)
                print("Account creation successful")
                #Display the user's ID number so that they know their ID number
                print(f"Your user ID is {user_id}")
            elif option=="2":
                this_user, user_id=manager.add_user(entered_name,entered_password,manager.nurses)
                print("Account creation successful")
                print(f"Your user ID is {user_id}")
            elif option=="3":
                this_user, user_id=manager.add_user(entered_name,entered_password,manager.admins)
                print("Account creation successful")
                print(f"Your user ID is {user_id}")
            elif option=="4":
                this_user, user_id=manager.add_user(entered_name,entered_password,manager.patients)
                print("Account creation successful")
                print(f"Your user ID is {user_id}")
            else:
                print("Invalid option")

    #Do the following if the user selects the 2nd option
    if option=="2":
        print("--- LOGIN PAGE ---")

        #Repeat for as long as user input is invalid (Data validation)
        error=True
        while error:
            try:
                entered_ID=int(input("ID: "))
                error=False
                print()
                #User input is valid therefore error==False so that the loop can be exited
            except ValueError:
                print("Please enter a valid ID number!")
                print()

        entered_password=input("password: ")

        print("Select your role:")
        print("1. Doctor")
        print("2. Nurse")
        print("3. Admin")
        print("4. Patient")

        option=input("option: ")
        print()

        if option=="1":
            #Remember, the log_in() function returns the user object if login is successful
            #The returned object is stored in this_user
            this_user=manager.log_in(entered_ID,entered_password,manager.doctors)
        elif option=="2":
            this_user=manager.log_in(entered_ID,entered_password,manager.nurses)
        elif option=="3":
            this_user=manager.log_in(entered_ID,entered_password,manager.admins)
        elif option=="4":
            this_user=manager.log_in(entered_ID,entered_password,manager.patients)
        else:
            print("Invalid option")

    #If option 1 or option 2 was selected and account-creation/log-in was successful then user is logged in either way
    if this_user:
        print("Login successful")
        if isinstance(this_user, doctor):
            #show the user the view/menu of a doctor if the user is a doctor
            #How should YOU use this section:
            #   -You will basically code up a menu for your class. If you are responsible for the doctor class,
            #   then your code will go in this block otherwise you must write your code in one of the blocks below
            #   -Ensure to include data validation and data verification as required
            #   -The user that is currently logged in is the object stored in the this_user variable
            #   -Obviously, depending on the user's type, they will be able to access certain features
            #   -To access a feature (coded as a function/procedure), a certain function/procedure must be called with reference to this_user
            #    for example (In the case the the logged in user is a doctor): this_user.some_function_from_the_doctor_class()
            #   -Make sure to import the class you are working on at the top of this file
            #   -You will also need to import this class (the one you are working on) in brain.py as well if it is not already there
            #   -If your class makes use of files other than the main careLogData.json file, then
            #    you might need to make changes to _load_data() and the system manager class
            #   -If you are unsure of how to implement your code in this section, have a look at how I did it (I did the admin one below).  
            #   -To test the program after you have integrated your code, run this file (main.py) as the main program,
            #   since this is the user interface module.
            #   -When you run the program, you will be asked to enter your details as an existing user, so you may
            #   obtain these details from the careLogData.json file. Alternatively you could just create your own user account
            #   by selecting option 1. Please do ensure that the number of nurse users in the file is always the same as the number of doctor users
            #   as there is a possibility that the program could break if they aren't equal.
            pass
        elif isinstance(this_user, nurse):
            #show the user the view/menu of a nurse if the user is a nurse
            print("--- NURSE PAGE ---")
            print("1. Record clinical observation")
            print("2. Edit patient log")
            print("3. Generate patient summary report")
            print("4. Delete patient log")

            option=input("option: ")

            if option=="1":
                error=True
                #Validation to ensure the user only inputs an integer value
                while error:
                    try:
                        patient_id=int(input("Patient ID: "))
                        error=False
                        print()
                        #User input is valid therefore error==False so that the loop can be exited
                    except ValueError:
                        print("Please enter a valid patient ID number!")
                        print()

                log_entry=input("Enter details: ")
                #Store the return message in the message variable
                message=this_user.record_clinical_observation(patient_id, log_entry)
                #print message
                print(message)

            elif option=="2":
                error=True
                while error:
                    try:
                        patient_id=int(input("Patient ID: "))
                        log_index=int(input("Log number: "))
                        error=False
                        print()
                        #User input is valid therefore error==False so that the loop can be exited
                    except ValueError:
                        print("Please enter a valid patient ID number and log number!")
                        print()

                log_entry=input("Enter details: ")
                message=this_user.edit_patient_log(patient_id,log_index,log_entry)
                print(message)

            elif option=="3":
                error=True
                while error:
                    try:
                        patient_id=int(input("Patient ID: "))
                        error=False
                        print()
                        #User input is valid therefore error==False so that the loop can be exited
                    except ValueError:
                        print("Please enter a valid patient ID number!")
                        print()

                message=this_user.generate_patient_summary_report(patient_id)
                print(message)

            elif option=="4":
                error=True
                while error:
                    try:
                        patient_id=int(input("Patient ID: "))
                        log_index=int(input("Log number: "))
                        error=False
                        print()
                        #User input is valid therefore error==False so that the loop can be exited
                    except ValueError:
                        print("Please enter a valid patient ID number and log number!")
                        print()

                message=this_user.delete_patient_log(patient_id,log_index)
                print(message)

            else:
                print("Invalid option.")

        elif isinstance(this_user, admin):
            #show the user the view/menu of an admin if the user is an admin
            print("--- ADMIN PAGE ---")
            print("1. See all new patients")
            print("2. Automatically assign staff to new patients")
            print("3. Change name")
            print("4. Change password")
            #ALSO ADD OPTION TO SEE PATIENT PREFERENCES

            option=input("option: ")

            if option=="1":
                #Display all new patients who have not been assigned staff (doctor and nurse)
                this_user.notify(manager.patients_without_doctors)
            elif option=="2":
                #Assign a nurse and a doctor to each new patient
                assigned=this_user.assign_staff_to_patient(manager.nurses,manager.doctors,manager.patients_without_doctors)
                #Print the statement that is returned from the function call which will indicate if assignment was successful or not
                print(assigned)
            elif option=="3":
                pass
            elif option=="4":
                pass
            else:
                print("Invalid option")
            
        elif isinstance(this_user, patient):
            #show the user the view/menu of a patient if the user is a patient
            print("--- PATIENT PAGE ---")
            print("1. Set my preferences")
            print("2. See my preferences")

            option=input("option: ")
            print()

            if option=="1":
                visiting_days = []
                day=""
                count=0
                #Allow the patient user to enter upto 3 preferred visiting days
                while day!="exit" and count<3:
                    print("Enter your preferred visiting days (upto 3) or type 'exit' to stop: ")
                    day=input(f"day {count + 1}: ")

                    if day!="exit":
                        visiting_days.append(day)
                        count+=1

                visiting_hours=input("Enter your preferred visiting hours (2:00 - 3:00 pm or 7:00 to 8:00 pm): ")
                language=input("Enter your preferred language: ")

                this_user.set_preferences(visiting_days, visiting_hours, language, manager.patient_preferences)
                print()
                print("Preferences have been saved")

            elif option=="2":
                this_user.display_patient_info(manager.patient_preferences)

            else:
                print("Invalid option.")

        manager.log_out()
        print()
        print("Successfully Logged out")
    else:
        print("Login failed")


if __name__=="__main__":
    main()