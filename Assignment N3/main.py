students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85), ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]

# Unique Grades
print('1. Unique Grades')
grades = []
for name, grade in students:
    grades.append(grade)
unique_grades = set(grades)
print(unique_grades)
print('== ' * 10)

# Top Performers'
print('2. Top Performers')
students.sort(key=lambda student: student[1])
print(f"{students[-1][0]} got the highest score - {students[-1][1]}.")
print(f"{students[-2][0]} got the second highest score - {students[-2][1]}.")
print(f"{students[-3][0]} got the third highest score - {students[-3][1]}.")
print('== ' * 10)

# Failed Students
print('3. Failed Students')
for name, grade in students:
    if grade < 51:
        print(f"{name} failed with {grade} points. Good luck next year, {name}!")
