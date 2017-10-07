#Pytest

class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignment = []
        self.grade = None

class Classroom():
    def __init__(self, class_name, date):
        self.roster = {}
        self.student_assignments = []
        pass

    def add_student(self, student):
        pass

    def remove_student(self, student):
        '''
        Receives a student object
        Adds student (object) to dictionary
        '''
        pass

    def add_assignment(self, assignment):
        pass

    def remove_assignment(self, assignment):
        pass
