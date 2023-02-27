class Party:
    def __init__(self,):
        self.people = []


command = input()
obj = Party()
while command != "End":
    obj.people.append(command)
    command = input()


print(f'Going: {", ".join(obj.people)}')
print(f"Total: {len(obj.people)}")
