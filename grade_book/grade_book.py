import student
import classroom

cs1 = classroom.Classroom("cs1")
juan = student.Student('juan', 1)
mondale = student.Student('mondale', 2)


cs1.add_student(juan)
cs1.add_student(mondale)
cs1.add_student_assignments('grade_book', 50, 2)
cs1.add_student_assignments('grade_book', 100, 1)
cs1.add_student_assignments('roulette', 80, 1)
print(cs1.roster[1].name, cs1.roster[1].get_assignment())
print(cs1.roster[2].name, cs1.roster[2].get_assignment())

print(juan.get_gpa())
print(cs1.get_gpa())

print(juan.get_assignment())
print(juan.assignment)
