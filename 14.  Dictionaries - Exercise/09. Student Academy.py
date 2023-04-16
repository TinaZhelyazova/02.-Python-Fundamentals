student_grades = {}
n = int(input())


for i in range(n):
    students_name = input()
    grade = float(input())

    if students_name not in student_grades:
        student_grades[students_name] = []
    student_grades[students_name].append(grade)


for key, value in student_grades.items():
    if sum(value) / len(value) < 4.5:
        continue
    print(f"{key} -> {sum(value) / len(value):.2f}")
