#Import all user classes and the json library
import json
#encrypter has been included here mainly for demonstration/proof of concept but has not been fully implemented throughout the entire program
import encrypter as e
from user_base_class import user
from doctor_class import doctor
from patient_class import patient
from admin_class import admin
from nurse_class import nurse

class SystemManager:
    """The main controller for all system logic and data handling."""

    def __init__(self, data_path1="careLogData.json", data_path2="patientPreferences.json"):
        self.data_path1 = data_path1
        self.data_path2 = data_path2
        #These lists store objects of each user_type
        self.doctors = []
        self.nurses = []
        self.admins = []
        self.patients = []
        #This is a dictionary to store dictionaries of patient preferences
        self.patient_preferences = {}
        #This list stores all patients that have not been assigned doctors and nurses
        self.patients_without_doctors=[]

        #Load data into memory when a system_manager object is instantiated
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""

        #Try...except block incase the data file is not found
        try:
            with open(self.data_path1, 'r') as f:
                data = json.load(f)

                for this_doctor in data.get("doctors",[]): 
                    #Instantiate each doctor using the doctor sub-class and append the doctor to the self.doctors list   
                    self.doctors.append(doctor(this_doctor["user_id"],this_doctor["name"],this_doctor["password"],corresponding_nurse=this_doctor["corresponding_nurse"],assigned_patients=this_doctor["assigned_patients"])) 
                
                for this_nurse in data.get("nurses",[]):
                    self.nurses.append(nurse(this_nurse["user_id"],this_nurse["name"],this_nurse["password"],this_nurse["patient_logs"],assigned_patients=this_nurse["assigned_patients"]))
                
                for this_admin in data.get("admins",[]):
                    #THE ENCRYPTER MODULE IS USED HERE TO DECRYPT PASSWORDS FROM THE JSON FILE AND STORE THEM IN MEMORY
                    self.admins.append(admin(this_admin["user_id"],this_admin["name"],e.decrypt(this_admin["password"])))

                for this_patient in data.get("patients",[]):
                    self.patients.append(patient(this_patient["user_id"],this_patient["name"],this_patient["password"]))

                for this_patient in data.get("Doctorless_patients",[]):
                    self.patients_without_doctors.append(patient(this_patient["user_id"],this_patient["name"],this_patient["password"]))                         

        except FileNotFoundError:
            print("Data file not found.")

        #Load patient preferences into memory from json file
        try:
            with open(self.data_path2, 'r') as f:
                data = json.load(f)

                self.patient_preferences = data
        except FileNotFoundError:
            print("Data file not found.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""

        #THE ENCRYPTER MODULE IS USED HERE TO ENCRYPT PASSWORDS AS THEY ARE STORED TO THE JSON FILE
        #Since the passwords (for admins only) stored in the JSON file are in encrypted form, 
        #you cannot use them directly when logging in.
        #The actual passwords for the 3 admins are as follows:
        # Liam Bernard's password: LB33
        # Ari Fring's password: WHOISARI
        # Mustafa Jason's password: ITSAMEE
        for this_admin in self.admins:
            this_admin.password=e.encrypt(this_admin.password)

        #Create a 'data_to_save' dictionary.
        data_to_save = {
            #Create a dictionary for each object's attributes and append this dictionary to a list
            #The list becomes a value to some key ("doctors", "nurses", etc)
            "doctors": [d.__dict__ for d in self.doctors],
            "nurses": [n.__dict__ for n in self.nurses],
            "admins": [a.__dict__ for a in self.admins],
            "patients": [p.__dict__ for p in self.patients],
            "Doctorless_patients": [dp.__dict__ for dp in self.patients_without_doctors]
        }

        #Write the data, including any changes, to the json file using the appropriate format
        with open(self.data_path1, 'w') as f:
            json.dump(data_to_save, f, indent=4)

        #Write the data, including any changes, to the json file using the appropriate format
        with open(self.data_path2, 'w') as f:
            json.dump(self.patient_preferences, f, indent=4)

    #Function that takes a user's ID,password and a list of objects (doctors, nurses etc) depending on what the user would have selected 
    #The function then verifies the user and
    #returns the user object if log in is successful otherwise 'None' is returned
    def log_in(self, entered_ID, entered_password, user_list):
        """Authenticates user and then returns a user object"""
        for this_user in user_list:
            if this_user.user_id==entered_ID and this_user.password==entered_password:
                return this_user
        return None

    #Procedure that calls _saves_data() to save changes to the JSON file when the user logs out
    def log_out(self):
        """Calles _save_data() to save changes to JSON file"""
        self._save_data()

    #Function that takes in a user_name, password and a list of objects depending on the user's type
    #The function returns the new user object as well as the object's ID after appending it to the appropriate list (doctors, nurses etc)
    def add_user(self, entered_name, entered_password, user_list):
        """Adds a user object to the appropriate user list and returns the new user object and its user ID"""
        #Obtain the ID of the last object in the list and increment it by 1 to give the new user an ID
        user_id=user_list[-1].user_id + 1

        #Check what type of object the list contains so as to append the new_user to the correct object list
        #isinstance() returns True when when the first parameter is of the type specified in the 2nd parameter
        #for example: isinstance(2, int) returns True whilst isinstance(False, str) returns False
        #Therefore only the code block where isinstance() returns True is executed
        if isinstance(user_list[0], doctor):
            self.doctors.append(doctor(user_id,entered_name,entered_password))
            return self.doctors[-1], user_id
        
        elif isinstance(user_list[0], nurse):
            self.nurses.append(nurse(user_id,entered_name,entered_password))
            return self.nurses[-1], user_id
        
        elif isinstance(user_list[0], admin):
            self.admins.append(admin(user_id,entered_name,entered_password))
            return self.admins[-1], user_id
        
        elif isinstance(user_list[0], patient):
            self.patients.append(patient(user_id,entered_name,entered_password))
            #Special case: Add the patient to the patient_without_doctors list so that they may be assigned a doctor and nurse
            self.patients_without_doctors.append(self.patients[-1])
            return self.patients[-1], user_id
        else:
            #This line will most likely never execute but is included as good programming practice
            return None, None
        
