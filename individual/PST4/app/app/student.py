from app.app.user import User

class StudentUser(User):
    """Represents a student, inheriting from the base User class."""
    # Takes the *enrolled_course_ids parameter which allows for multiple course ids to be
    #part of the instantion of a student object
    def __init__(self, user_id, name, enrolled_course_ids):
        # TODO: Call the parent class's __init__ method using super().
        super().__init__(user_id, name)
        # TODO: Initialize an empty list called 'enrolled_course_ids' to store the IDs of courses.
        self.enrolled_course_ids = enrolled_course_ids

    def get_enrolled_course_ids(self):
        return self.enrolled_course_ids
