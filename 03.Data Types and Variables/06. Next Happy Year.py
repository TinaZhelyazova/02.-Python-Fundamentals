year = int(input())
is_happy_year = False

while not is_happy_year:
    year += 1
    set_year = set()
    year = str(year)
    for i in range(len(year)):
        set_year.add(year[i])

    year = int(year)
    if len(set_year) == len(str(year)):
        is_happy_year = True
        break;

print(int(year))

