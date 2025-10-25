from user_base_class import user

class admin(user):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)

    #This function is defined but not currently in use anywhere in the program
    def remove_user(self, entered_ID, user_list):
            for this_user in user_list:
                if entered_ID==user_list.user_id:
                    user_index=user_list.index(this_user)
                    user_list.pop(user_index)
                    return True
            return False
    
    #This function simply displays all patients that have not been assigned doctors and nurses
    #It is named 'notify' as it acts as a kind of notification for the admin so 
    #that they can assign the new patients doctors and nurses
    def notify(self, doctorless_patients_list):
        """Displays a list of new patients"""
        for patient in doctorless_patients_list:
            print(f"Patient name:{patient.name}   Patient ID:{patient.user_id}")
    
    def assign_staff_to_patient(self, nurses_list, doctors_list, doctorless_patients_list):
        """Assigns staff (nurses and doctors) to each patient in the doctorless_patients list """
        #Note: For this function to not break, there needs to be the same number of nurses as there are doctors
        if len(doctorless_patients_list)==0:
            return "No new patients to be assigned staff"
            
        for i in range(len(nurses_list)):
            if len(doctorless_patients_list)>0:
                #No nurse or doctor can be assigned more than 10 patients
                if len(nurses_list[i].assigned_patients)<10:
                    nurses_list[i].assigned_patients.append(doctorless_patients_list[0].user_id)
                else:
                    return "All nurses are occupied"

                if len(doctors_list[i].assigned_patients)<10:
                    doctors_list[i].assigned_patients.append(doctorless_patients_list[0].user_id)
                    #Since this doctor has the same assigned_patients as this nurse, this nurse becomes a corresponding nurse to the doctor
                    #See the doctor class for more detailed comments about this
                    doctors_list[i].corresponding_nurse = nurses_list[i].user_id
                else:
                    return "All doctors are occupied"

                #One patient has been assigned a doctor and a nurse therefore they can be removed from the doctorless_patients list
                doctorless_patients_list.pop(0)
            else:
                return "All new patients have been assigned a nurse and a doctor"                  

