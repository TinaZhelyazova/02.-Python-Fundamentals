first = int(input())  # the number of students that the first employee can help per hour.
second = int(input())  # the number of students that the second employee can help per hour.
third = int(input())  # the number of students that the third employee can help per hour.
all_students = int(input())  # all students that need to be answered

answered_students_per_hour = first + second + third
all_students_answered = 0
hours_needed = 0

while all_students_answered != all_students:
    for i in range(3):
        if all_students_answered >= all_students:
            break
        all_students_answered += answered_students_per_hour
        hours_needed += 1
    if all_students_answered >= all_students:
        break
    else:
        hours_needed+=1

print(f"Time needed: {hours_needed}h.")
