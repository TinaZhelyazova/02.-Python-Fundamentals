number_of_electrons = int(input())
counter = 1
shells = []

while True:
    formula = 2*(counter**2)
    if number_of_electrons <= formula:
        shells.append(number_of_electrons)
        break
    shells.append(formula)
    number_of_electrons -= formula
    counter += 1
print(shells)
