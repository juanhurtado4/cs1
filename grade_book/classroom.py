# format for date
# date = {
# "CS1": [('wed', '10 am', '11 am'), ('fri', '9 am', '5 pm')],
# }
# print(date["CS1"][0])

#student_assignment = 'student_id': [('protocols', 99), ('mood tracker', 85)]

'''
create
read
update
delete

be able to give everyone one assignment or one student
'''


class Classroom():
    def __init__(self, class_name):
        self.class_name = class_name
        # self.class_dates = {}
        self.roster = {} # Student id as key value student object itself
        self.student_assignments = []
        # self.student_grades = {} # Student_id key: Value: tuple of assignment and grade
        pass

    def add_student_assignments(self, roster, assignment, grade, student_id=None):
        # iterate through dictionary of students and call student add
        if student_id != None:
            self.roster[student_id].add_assignment(assignment, grade)
        elif student_id == None:
            for student in self.roster.keys():
                self.roster[student].add_assignment(assignment, grade)

    def add_student(self, student, student_id, classroom):
        '''
        Function doesn't return anything
        '''
        classroom.roster[student_id] = student

    def remove_student(self, student, classroom):
        classroom.roster.pop(student)


def main():
    def __init__(self, name):
        self.name = name

    def create_classroom(self, class_name):
        return Classroom(class_name)




mike = Teacher('mike')
mike_cs1 = mike.create_classroom('cs1')
print(mike_cs1.class_name)
