from nurse_class import nurse

#This class inherits from nurse unlike the others which inherit from the user_base_class
class doctor(nurse):
    #Corresponding_nurse is a variable to store the ID of the nurse who has the same assigned_patients list as the doctor
    #Every doctor has a corresponding nurse that shares the same assigned patients_list
    #Patient_logs is a dictionary where a key is a patient_ID and the value is a list of the patients log history
    def __init__(self, user_id, name, password, corresponding_nurse=None, patient_logs={}, assigned_patients=[]):
        super().__init__(user_id, name, password, patient_logs, assigned_patients)
        self.corresponding_nurse = corresponding_nurse

    #Function to initialise patient_logs
    #It does this by finding the corresponding nurse and copying this dictionary since this nurse shares the same
    #patients as the doctor
    def fetch_patient_logs(self, nurses_list):
        #Check if the doctor has a corresponding nurse
        #Not having a corresponding nurse effectively means the doctor hasn't been assigned any patients
        if self.corresponding_nurse:
            for this_nurse in nurses_list:
                if this_nurse.user_id == self.corresponding_nurse:
                    #Copy the dictionary from the corresponding nurse and exit loop
                    self.patient_logs = this_nurse.patient_logs
                    break
        

        
