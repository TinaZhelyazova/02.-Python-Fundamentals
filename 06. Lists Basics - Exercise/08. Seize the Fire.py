cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells_for_print = []

# High = 89#Low = 28#Medium = 77#Low = 23
# 1250

for i in cells:
    arguments = i.split(" = ")
    type_of_fire = arguments[0]
    water_needed = int(arguments[1])
    if water < water_needed:
        continue

    if type_of_fire == "Low" and (1 <= water_needed <= 50):
        water -= water_needed
        total_fire += water_needed
        cells_for_print.append(water_needed)
        effort += water_needed
    if type_of_fire == "Medium" and (51 <= water_needed <= 80):
        water -= water_needed
        total_fire += water_needed
        cells_for_print.append(water_needed)
        effort += water_needed
    if type_of_fire == "High" and (81 <= water_needed <= 125):
        water -= water_needed
        total_fire += water_needed
        cells_for_print.append(water_needed)
        effort += water_needed

effort = float(effort * 0.25)

print(f"Cells:")
for i in cells_for_print:
    print(f" - {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
