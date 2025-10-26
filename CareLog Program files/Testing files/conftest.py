import pytest
from CareLog_main_files.brain import SystemManager


#THIS FILE IS NEEDED AS ITS READEN AUTOMATICALLY BY PYTEST
# AS EVERYTIME TEST_SYSTEM IS CALLED PYTEST AUTOMATICALLY READS IT INSTEAD OF HAVING TO ANUALLY CREATE A SYSTEM MANAGER
# CLASS EACH TIME FOR EACH UNIT TEST

# TLDR: Sharing fixtures for all pytest files

#using fixture to make a clean environment for each test function
@pytest.fixture
# since this is on the testing branch, no need to create testing files as we can use the existing json files 
def test_SystemManager():
    return SystemManager(data_path1="../CareLog_main_files/careLogData.json", data_path2="../CareLog_main_files/patientPreferences.json")