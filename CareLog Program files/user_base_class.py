class user:
    #CONSTRUCTOR HAS BEEN CHANGED SUCH THAT login_state IS NOW A KEYWORD PARAMETER
    #This change was made particularly for the add_user function
    def __init__(self,user_id,name,password):
        self.name=name
        self.user_id=user_id
        self.password=password
        #self.login_state=False

#The following classes have been created only for testing the brain.py module
#They will not be part of the final program. Instead, we will have separate modules for each class.
class doctor(user):
    def __init__(self, user_id, name, password, assigned_patients=[]):
        super().__init__(user_id, name, password)
        self.assigned_patients=assigned_patients

class patient(user):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)

class nurse(user):
    def __init__(self, user_id, name, password, assigned_patients=[]):
        super().__init__(user_id, name, password)
        self.assigned_patients=assigned_patients

class admin(user):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)