class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    @staticmethod
    def get_average_grade(grades):
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)

    def __str__(self):
        return f'Name: {self.name}, Grades: {self.grades}, Average: {self.get_average_grade(self.grades)}'

class Classroom:
    def __init__(self, students):
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):
        top_students = sorted(self.students, key=lambda student: Student.get_average_grade(student.grades), reverse=True)
        return top_students[:3]

    def get_failed_students(self):
        failed_students = []
        for student in self.students:
            if Student.get_average_grade(student.grades) < 51:
                failed_students.append(student)
        return failed_students

    def __str__(self):
        top_students = ', '.join(str(student) for student in self.get_top_students())
        failed_students = ', '.join(str(student) for student in self.get_failed_students())
        return f"List of top students: {top_students}, Failed students: {failed_students}"

# Testing how it works:
student1 = Student('Sali', [100, 90, 30, 11, 98])
student2 = Student('Ana', [28, 9, 16, 28, 80])
student3 = Student('Nino', [100, 90, 70, 20, 10])
student4 = Student('Levan', [28, 9])
student5 = Student('Guram', [51, 10, 40])
classroom1 = Classroom([student1, student2, student3, student4, student5])

failed_students = classroom1.get_failed_students()
top_students = classroom1.get_top_students()

print([str(student) for student in top_students])
print([str(student) for student in failed_students])
