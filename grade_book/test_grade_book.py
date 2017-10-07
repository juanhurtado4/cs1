from  classroom import Classroom
from  student import Student

import pytest

def test_init_student():
    student = Student('First Lastname', 1)
    assert student.name == 'First Lastname'
    assert student.student_id == 1
    assert student.grade == None
    assert len(student.assignment) == 0

def test_get_assignments_student():
    # self.assignment = {'juan': [['assignment1', 67], ['assignment2', 99]]}
    assert assignments == ['assignment1', 'assignment2']
