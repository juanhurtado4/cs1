#Pytest
import student
import classroom


cs1 = classroom.Classroom("cs1")
juan = student.Student('juan', 1)
cs1.add_student(juan, juan.student_id)
cs1.add_student_assignments('grade_book', 0, 1)
cs1.add_student_assignments('roulette', 0, 1)
print(cs1.roster[1].get_assignment())
