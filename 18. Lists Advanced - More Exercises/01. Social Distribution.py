population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

while True:
    count = len(population)
# първо проверяваме дали е възможно разпределянето на богатството
    if sum(population) < min_wealth * count:
        print("No equal distribution possible")
        break

    if all(i >= min_wealth for i in population):
        print(population)
        break
# сега започваме да разпределяме богатството като започнем да даваме от най-голямото число на най-малкото

    max_num = max(population)
    min_num = min(population)
    index_of_max = population.index(max_num)
    index_of_min = population.index(min_num)
    if min_num < min_wealth:
        if max_num > min_wealth:
            needed_wealth_to_give = min_wealth - min_num
            population.remove(max_num)
            population.remove(min_num)
            max_num -= needed_wealth_to_give
            min_num += needed_wealth_to_give
            population.insert(index_of_max, max_num)
            population.insert(index_of_min, min_num)

