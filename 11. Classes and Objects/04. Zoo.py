class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f'Mammals in {self.name}: {", ".join(self.mammals)} \n'
        elif species == "fish":
            result += f'Fishes in {self.name}: {", ".join(self.fishes)} \n'
        elif species == "bird":
            result += f'Birds in {self.name}: {", ".join(self.birds)} \n'

        result += f"Total animals: {Zoo.__animals}"
        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
n = int(input())

for i in range(n):
    animal_info = input().split()
    type_of_animal = animal_info[0]
    name_of_animal = animal_info[1]
    zoo.add_animal(type_of_animal, name_of_animal)

info = input()
print(zoo.get_info(info))
