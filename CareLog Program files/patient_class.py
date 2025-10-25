from user_base_class import user

class patient(user):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)

    #patients_preferences_dict is a dictionary of dictionaries of patient preferences (see the patientPreferences.json file)
    def set_preferences(self, visiting_days, visiting_hours, language, patients_preferences_dict):
        """
        Saves a patients preferences to a dictionary
        """

        #Check the patient has already set their preferences
        #if they have, then access their dictionary and make the new changes
        #otherwise, create an empty dictionary with the key being their user_id and the value, an empty dictionary
        #then set the preferences and add to the patient's dictionary
        if str(self.user_id) in patients_preferences_dict:
            patients_preferences_dict[str(self.user_id)]["preferred_visiting_days"] = visiting_days
            patients_preferences_dict[str(self.user_id)]["preferred_visiting_hours"] = visiting_hours
            patients_preferences_dict[str(self.user_id)]["language"] = language
        else:
            patients_preferences_dict[str(self.user_id)] = {}
            patients_preferences_dict[str(self.user_id)]["preferred_visiting_days"] = visiting_days
            patients_preferences_dict[str(self.user_id)]["preferred_visiting_hours"] = visiting_hours
            patients_preferences_dict[str(self.user_id)]["language"] = language

    
    def display_patient_info(self, patients_preferences_dict):
        """
        Displaying the patient's information and preferences
        """
        #Check if the user's preferences dictionary exists
        #If yes, then assign values from the dictionary to the appropriate attributes
        if str(self.user_id) in patients_preferences_dict:
            preferred_visiting_days = patients_preferences_dict[str(self.user_id)]["preferred_visiting_days"]
            preferred_visiting_hours = patients_preferences_dict[str(self.user_id)]["preferred_visiting_hours"]
            language_preference = patients_preferences_dict[str(self.user_id)]["language"]

            #print the info
            print("PATIENT INFORMATION AND PREFERENCES")
            print("="*20)
            print(f"Name: {self.name}")
            print(f"Preferred Visiting Days: {', '.join(preferred_visiting_days)}")
            print(f"Preferred Visiting Hours: {preferred_visiting_hours}")
            print(f"Communication Preference: {language_preference}")

        else:
            print("You have not entered any preferences")
