class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # Structure for student assignment:
        # Student_assignment = 'assignment_name': grade
        self.assignment = {} # Assignment should be modeled as above

    def add_assignment(self, student_id, assignment, grade):
        '''
        Student_id & Grade: Integer. Assignment: String
        Function adds new assignment to the dictionary of assignments.
        Returns none
        '''
        self.assignment[student_id] = [assignment, grade]

    def get_assignment(self, student_id):
        '''
        Student_id: Integer.
        Returns a nested list of assignments.
        '''
        assignments = []
        # list_assignments = {'juan': [['assignment1', 67], ['assignment2', 99]]} #DELETE
        # for arr_assignments in list_assignments.values():
        for arr_assignments in self.assignment.values():
            for single in arr_assignments:
                assignments.append(single[0])

        return assignments

    def update_assignment(self, new_assignment, old_assignment):
        for index, assignment in enumerate(self.assignment[self.student_id]):
            if assignment[0] == old_assignment:
                self.assignment[self.student_id][index][0] = new_assignment





'''
crud assignment
'''
