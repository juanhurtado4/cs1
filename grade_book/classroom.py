class Classroom():
    def __init__(self, class_name):
        self.class_name = class_name
        self.roster = {} # Student id as key value student object itself

    def get_gpa(self):
        '''
        Returns the avg grade for the entire class_name
        based on each individual student grades
        '''
        final = 0
        for student in self.roster.values():
            final += student.get_gpa()
        return final / len(self.roster)

    def add_student_assignments(self, assignment, grade, student_id=None):
        '''
        Assignment type: String
        Grade & Student ID type: Int
        Function adds student assignment to individual student if student id provide
        If not it will add assignment to all students
        Returns void
        '''
        if student_id != None:
            self.roster[student_id].add_assignment(assignment, grade)
        elif student_id == None:
            for student in self.roster.keys():
                self.roster[student].add_assignment(assignment, grade)

    def delete_student_assignment(student, assignment):
        '''
        Assignment type: String
        Student type: Class
        Function deletes assignment
        Returns void
        '''
        student.delete_assignment(assignment)

    def add_student(self, student):
        '''
        Student type: Class
        Function adds student to dictionary of roster
        Returns void

        '''
        self.roster[student.student_id] = student

    def remove_student(self, student):
        '''
        Student type: Class
        Function removes student from roster dictionary
        Returns void
        '''
        self.roster.pop(student)
