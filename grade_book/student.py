class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # Structure for student assignment: 'assignment_name': grade
        self.assignment = {}

    def __str__(self):
        '''
        Function overides default object string interpretation
        '''
        return "This student's name is {name}".format(name=self.name)

    def add_assignment(self, assignment, grade):
        '''
        Grade type: Integer
        Assignment type: String
        Function adds new assignment to the dictionary of assignments.
        Returns none
        '''
        self.assignment[assignment] = grade

    def get_assignment(self):
        '''
        Function returns a dictionary of assignments.
        '''
        return self.assignment
        # return [assignment for assignment in self.assignment.keys()]

    def delete_assignment(self, assignment):
        '''
        Assignment type: String
        Function deletes assignment from dictionary of student assignments
        '''
        self.assignment.pop(assignment)

    def update_assignment(self, new_assignment, old_assignment, grade):
        '''
        New Assignment & Old type: String
        Grade type: Int
        Function updates assignments
        Returns void
        '''
        self.delete_assignment(old_assignment)
        self.add_assignment(new_assignment, grade)

    def get_gpa(self):
        '''
        Function returns the avg grade for all the assignments
        '''
        final = 0
        for grade in self.assignment.values():
            final += grade
        return final / len(self.assignment)
