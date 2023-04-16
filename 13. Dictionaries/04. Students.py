courses = {}
command = input().split(":")

while len(command) > 1:
    name = command[0]
    id = command[1]
    course = command[2]

    if course not in courses.keys():
        courses[course] = []
    courses[course].append(f"{name} - {id}")
    command = input().split(":")

searched_course = command[0].replace("_", " ")
for students in courses[searched_course]:
    print(students)
