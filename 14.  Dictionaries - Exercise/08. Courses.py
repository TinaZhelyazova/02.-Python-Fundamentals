courses = {}
command = input()

while True:
    if command == "end":
        break

    args = command.split(" : ")
    course_name = args[0]
    student_name = args[1]
    #students = []
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for key, values in courses.items():
    print(f"{key}: {len(values)}")
    for value in values:
        print(f"-- {value}")

