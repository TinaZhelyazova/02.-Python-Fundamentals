class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1
        return

    def get_average_grade(self):
        return sum(self.grades)/(22 - Class.__students_count)

    def __repr__(self):
        students = ", ".join(self.students)
        avg_grade = self.get_average_grade()
        return f"The students in {self.name}: {students}. Average grade: {avg_grade:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
