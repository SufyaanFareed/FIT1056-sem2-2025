from user_base_class import user

class admin(user):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)

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
        for patient in doctorless_patients_list:
            print(f"Patient name:{patient.name}   Patient ID:{patient.user_id}")
    
    def assign_staff_to_patient(self, nurses_list, doctors_list, doctorless_patients_list):
        #Note: For this function to not break, there needs to be the same number of nurses as there are doctors
        if len(doctorless_patients_list)==0:
            return "No new patients to be assigned staff"
            
        for i in range(len(nurses_list)):
            if len(doctorless_patients_list)>0:
                if len(nurses_list[i].assigned_patients)<10:
                    nurses_list[i].assigned_patients.append(doctorless_patients_list[0].user_id)
                else:
                    return "All nurses are occupied"

                if len(doctors_list[i].assigned_patients)<10:
                    doctors_list[i].assigned_patients.append(doctorless_patients_list[0].user_id)
                else:
                    return "All doctors are occupied"

                doctorless_patients_list.pop(0)
            else:
                return "All new patients have been assigned a nurse and a doctor"                  

