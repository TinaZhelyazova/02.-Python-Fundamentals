quantity_of_decorations = int(input())
days_left = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
budget = 0
spirit = 0


for day in range(1, days_left+1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        budget += ornament_set * quantity_of_decorations
        spirit += 5
    if day % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity_of_decorations
        spirit += 13
    if day % 5 == 0:
        budget += tree_lights * quantity_of_decorations
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += tree_garland+tree_lights +tree_skirt
if day % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
