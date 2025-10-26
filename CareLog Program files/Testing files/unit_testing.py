import pytest
from CareLog_main_files.brain import SystemManager
from CareLog_main_files.patient_class import patient

''' - -- - - - - - - LOG IN TEST - - - - - - - - - '''

# ! testing Login Success
def test_login_success(test_SystemManager):
    # ARRANGE: Using Test_systemMAnager from the fixture
    
    #ACT: Calling the method Log in to test
    user = test_SystemManager.log_in(1, "Alice123J0hn", test_SystemManager.doctors)
    
    # ASSERT: Making sure the login is successful
    assert user is not None
    assert user.user_id == 1
    assert user.name == "Alice Johnson"


# ! testing login with wrong password
def test_login_wrong_password(test_SystemManager):
    # ARRANGE: Using Test_SysteMManger from the fixture
    # ACT: CAlling the login method to test
    user = test_SystemManager.log_in(1, "wrongpass", test_SystemManager.doctors)
    
    # ASSERT: make sure user is not found 
    assert user is None

# ! Testing with a NON existent user
def test_login_nonexistent_user(test_SystemManager):
    # ARRANGE: Using the test_SystemManager
    # ACT: calling the login method to test
    user = test_SystemManager.log_in(100, "Alice123J0hn", test_SystemManager.doctors)
    
    # ASSERT: making sure user is not found
    assert user is None


""" - - - - -  NURSE TEST - - - - - - """

# ! Testing a Successful adding log for patient
def test_nurse_add_patient_log(test_SystemManager):
    # ARRANGE: using test_Systemmanager from the fixture
    
    # ACT: Get the Nurse
    nurse = test_SystemManager.nurses[0]
    
    # ACT 2: Get the add patient Log method to test
    message = nurse.add_patient_log(4, "Patient has cancer and might die from brain cancer")
    
    # ASSERT: Make sure added is returned and Entry for patient ID 4 is in logs
    assert "Added" in message
    assert "4" in nurse.patient_logs

# ! Testing a nurse where the patient is NOT assigned
def test_nurse_add_log_unassigned_patient(test_SystemManager):
    #ARRANGE: Using Test_systemManager from the fixture
    
    #ACT: Getting the nurse to be tested
    nurse = test_SystemManager.nurses[0]
    
    #ACT 2: Making the nurse add to the paitnet log to test
    message = nurse.add_patient_log(420, "Some observation")
    
    # ASSERT: make sure paitnet is not found and "Not Found" is returned
    assert "Not Found" in message

# ! Testing a Nurse recording clinical observation
def test_nurse_record_observation(test_SystemManager):
     #ARRANGE: Using Test_systemManager from the fixture
     
     #ACT: getting the nurse itself
    nurse = test_SystemManager.nurses[0]
    
    #ACT 2: Getting the nurse to test the record clinical observation method
    message = nurse.record_clinical_observation(4, "Dead")
    
    # ASSERT: Make sure Added is returned and Observation for that specific patient is there
    assert "Added" in message
    assert "Dead" in nurse.patient_logs["4"][-1]

# ! Testing of the nurse editing patient logs
def test_nurse_edit_patient_log(test_SystemManager):
         #ARRANGE: Using Test_systemManager from the fixture
         
        #ACT: getting the nurse from the test system
    nurse = test_SystemManager.nurses[0]
    
    # ACT 2: getting the nurse to call the edit patient log method
    message = nurse.edit_patient_log(4, 0, "Alive again")
    
    # ASSERT: make sure it returned Updated and the log is now "Alive Again"
    assert "Updated" in message
    assert "Alive again" in nurse.patient_logs["4"][0]

# ! Testing of th enurse deleting atient logs
def test_nurse_delete_patient_log(test_SystemManager):
    #ARRANGE: Using Test_systemManager from the fixture
    #ACT: Getting the nurse 
    nurse = test_SystemManager.nurses[0]
    #ACT: Store the amount of logs before deletion to be ASsert tested later
    log_amount_before_deletion = len(nurse.patient_logs["4"])
    #ACT 2: getting the nurse to delete that patient log
    message = nurse.delete_patient_log(4, 0)
    #ASSERT: Make sure it returns deleted 
    assert "Deleted" in message
    # makes sure that Log entries are Less by 1
    assert len(nurse.patient_logs["4"]) == log_amount_before_deletion - 1


''' - - - - - - ADMIN TESTING - - - - - - - -'''
# ! Testing admin assigning staff successfully
def test_admin_assign_success(test_SystemManager):
    # ARRANGE: Using Test system manager from fixture
    #ACT: ASSIGNING A NEW PATIENT to the SYSTEM, A PATIENT THAT ISNT ASSIGNED TO ANY DOCTOR
    new_patient = patient(123, "Jjamal Jaquavios the Third", "123")
    test_SystemManager.patients_without_doctors.append(new_patient)
   
    # ACT 2: getting teh admin to call the assign staff to patient method
    admin = test_SystemManager.admins[0]
    message = admin.assign_staff_to_patient(test_SystemManager.nurses, test_SystemManager.doctors, test_SystemManager.patients_without_doctors)
    
    #ASSERT: Make sure the patient is there for the doctor and nurse and return message is correctly matched
    assert "All new patients have been assigned a nurse and a doctor" in message
    assert 123 in test_SystemManager.nurses[0].assigned_patients
    assert 123 in test_SystemManager.doctors[0].assigned_patients



# ! testing assigning when theres no patients to assign
def test_admin_assign_no_patients(test_SystemManager):
    # ARRANGE: Using Test system manager from fixture
    
    #ACT: getting the admin
    admin = test_SystemManager.admins[0]
    
    # ACT 2; setting patients without doctors to empty
    test_SystemManager.patients_without_doctors = []
    
    #ACT 3: assigning the patients 
    message = admin.assign_staff_to_patient(test_SystemManager.nurses, test_SystemManager.doctors, test_SystemManager.patients_without_doctors)
    
    # ASSERT: Make sure it Returns "no new patients"
    assert "No new patients" in message

""" -  - - - - - - PATIENT TEST  - - - - -"""

# ! Testing of patient setting preferences
def test_patient_set_preferences(test_SystemManager):
    # ARRANGE: Using Test system manager from fixture
    
    # ACT: Get patient number 5 (index 4)
    patient = test_SystemManager.patients[4]
    
    # ACT: Get the patient to set their preferences
    patient.set_preferences( "1234", "123", "eng", test_SystemManager.patient_preferences)
    
    # ASsert make sure the preferences are updated
    assert test_SystemManager.patient_preferences["5"]["preferred_visiting_hours"] == "123"
    assert test_SystemManager.patient_preferences["5"]["preferred_visiting_days"] == "1234"
    assert test_SystemManager.patient_preferences["5"]["language"] == "eng"


# ! Testing of patient updating preferences
def test_patient_update_preferences(test_SystemManager):
    # ARRANGE: Using Test system manager from fixture
    
    # ACT: getting patient 5 (index 4)
    patient = test_SystemManager.patients[4]
    
    # ACT: Updating the preferences with set method
    patient.set_preferences("joe1234", "joe123", "joe", test_SystemManager.patient_preferences)
    
    #assert: make sure the preferences are all updated
    assert test_SystemManager.patient_preferences["5"]["preferred_visiting_hours"] == "joe123"
    assert test_SystemManager.patient_preferences["5"]["preferred_visiting_days"] == "joe1234"
    assert test_SystemManager.patient_preferences["5"]["language"] == "joe"

# ! Testing of patient viewing preferences when they have not set any
def test_patient_display_no_preferences(test_SystemManager):
    # ARRANGE: Using Test system manager from fixture
    # ACT: getting patient with NO set preferences
    patient = test_SystemManager.patients[6]
    # ACT 2: getting patient to display info when theres none
    message = patient.display_patient_info(test_SystemManager.patient_preferences)
    
    assert "Haven't entered any preferences" in message
    
