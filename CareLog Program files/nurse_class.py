from user_base_class import user
#from brain import SystemManager
from datetime import datetime 

class nurse(user):
    #CHANGE BY ME in instantiation parameters
    def __init__(self, user_id, name, password, patient_logs, assigned_patients=[]):
        super().__init__(user_id, name, password)
        self.assigned_patients = assigned_patients
        self.patient_logs = patient_logs
        #self.manager = SystemManager()

    # checks for if a patient exists in the system database (list)
    def _patient_exists(self, patient_id):
        #original: in self.manager.patients:
        for this_id in self.assigned_patients:
            if this_id == patient_id:
                return True
        return False

    # checks if the patient exists before editing it, if patient log doesn't exist then make one
    def add_patient_log(self, patient_id, log_entry):
        if not self._patient_exists(patient_id):
            return f"Patient ID {patient_id} Not Found"

        #caution check in case patient_id logs doesnt exist
        if patient_id not in self.patient_logs:
            self.patient_logs[patient_id] = []

        # get the log number for ordering the logs
        log_number = len(self.patient_logs[patient_id]) + 1

        # grab the current time in Year Month Day, Hour Minute Second format
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # put them all into one single entry
        formatted_entry = f"{log_number}. [{timestamp}] {log_entry}"

        #append the entry and return success message
        self.patient_logs[patient_id].append(formatted_entry)
        return f"Patient ID {patient_id} Log Entry Added"

    # delete patient method, checks if patient exists before deleting
    def delete_patient_log(self, patient_id, log_index):
        #checks if patient id exists
        if not self._patient_exists(patient_id):
            return f"Patient ID {patient_id} Not Found"
        
        patient_id=str(patient_id)
        #checks if the log exists
        if patient_id in self.patient_logs:
            #delete that log
            self.patient_logs[patient_id].pop(log_index)
            #return success message
            return f"Patient ID {patient_id} Log Deleted"
        #otherwise return error message
        return f"No log found for Patient ID {patient_id}"

    # editing patient log, checks if patient exists before editing
    def edit_patient_log(self, patient_id, log_index, new_entry):
        if not self._patient_exists(patient_id):
            return f"Patient ID {patient_id} Not Found"

        #Convert patient_id from int to str as for the following code to work 
        # (patient id is stored as string in json file not int)
        patient_id=str(patient_id)
        #checks if patient id exists in the patient log
        if patient_id in self.patient_logs:
            # change timestamp of the edited log
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #change message as well and log entry index (to be newer)
            self.patient_logs[patient_id][log_index] = f"{log_index + 1}. [{timestamp}] {new_entry}"
            return f"Patient ID {patient_id} Log Updated"

        return f"No log found for Patient ID {patient_id}"

    # checks if patient exists before adding an entry log (new one)
    def record_clinical_observation(self, patient_id, observation):
        if not self._patient_exists(patient_id):
            return f"Patient ID {patient_id} Not Found"
        return self.add_patient_log(patient_id, f"Observation: {observation}")

    # generate a list of summary reports, but first check if patient id exists in database
    def generate_patient_summary_report(self, patient_id):
        if not self._patient_exists(patient_id):
            return f"Patient ID {patient_id} Not Found"

        #Convert patient_id from int to str as for the following code to work 
        # (patient id is stored as string in json file not int)
        patient_id=str(patient_id)
        #checks if patient id exists and the logs exists and is correct
        if patient_id in self.patient_logs and self.patient_logs[patient_id]:
            # return the entire log well formatted (each log is each new line)
            return "\n".join(self.patient_logs[patient_id])

        #print(self.patient_logs["4"])
        #error message if no logs are avaliable
        return f"No Patient Logs Available for ID {patient_id}"

    def nurse_notifications(self):
        pass
