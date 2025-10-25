***Carelog program guide on how to run the program***

*Folder structure:*

At present all files are kept in one single folder as follows:

Carelog Program files  
	user\_base\_class.py  
	admin\_class.py  
	patient\_class.py  
	nurse\_class.py  
	doctor\_class.py  
	Brain.py  
	gui.py  
	encrypter.py  
	carelogData.json  
	patientPreferences.json

*Running the program:*

Brief description of each file:

- user\_base\_class.py, admin\_class.py, patient\_class.py, nurse\_class.py, doctor\_class.py:  
    
  The User\_base\_class file contains the user base class from which all the other classes inherit their basic attributes. All other classes contain, in addition to their inherited attributes, their own unique attributes as well as associated methods that will be available to the user object of that class.  
    
- encrypter.py:  
    
  This file contains functions for encrypting and decrypting data. In our program, it is used for encrypting and decrypting passwords. Note that, that it is only used for objects of the admin class and not all classes for demonstration purposes. Implementing encryption for objects of all classes would mean that we would have to remember/store the unencrypted passwords elsewhere for testing purposes. So encryption/decryption has been included only for demonstration purposes rather than being implemented throughout the whole program.  
    
- patientPreferences.json and carelogData.json:  
    
  These are data files. Carelog.json stores, amongst other information, the passwords, usernames and IDs of each user. As mentioned above, the passwords of admin user’s passwords are stored in encrypted form, therefore if you wish to run the program as an admin, then you might need the following unencrypted passwords for the following admin users:  
    
  name:Liam Bernard		password:LB33  
  name:Ari Fring		password:WHOISARI  
  name:Mustafa Jason	password:ITSAMEE  
    
  patientPreferences.json simply stores each patient user’s preferences  
    
- Brain.py:

	This file contains a class, systemManager, that is responsible for loading data  from the JSON files into memory and saving data to the JSON files. It is also responsible for adding new users as well as login and logout functions.

- gui.py:  
    
  This is the file that launches the user interface when it is run via “streamlit run gui.py”.


**In order to run the program, gui.py must be run. In order to do this, streamlit run gui.py must be entered in the terminal which will then open the UI in a browser.  When the program is run, you can either choose to login as an existing user or create a new user account. If you choose the former,you will be asked to enter ID,password and user type. You can obtain these details from the carelogdata.json file. The exception being for users of the admin class for reasons mentioned earlier. At the moment, the program only has one save point which is when the user logs out and returns to the login page. This means that after any change is made, the user will have to log-out and then log back in to see the changes. Thank you for reading\!\!**

   
