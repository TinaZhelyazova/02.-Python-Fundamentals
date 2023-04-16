material_dict = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while not obtained:
    materials = input().split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1].lower()

        if material in material_dict.keys():
            material_dict[material] += quantity
        else:
            material_dict[material] = quantity

        if material_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            shards_quantity = material_dict["shards"] - 250
            material_dict["shards"] = shards_quantity
            obtained = True
        elif material_dict["fragments"] >= 250:
            fragments_quantity = material_dict["fragments"] - 250
            material_dict["fragments"] = fragments_quantity
            print("Valanyr obtained!")
            obtained = True
        elif material_dict["motes"] >= 250:
            motes_quantity = material_dict["motes"] - 250
            material_dict["motes"] = motes_quantity
            print("Dragonwrath obtained!")
            obtained = True
        if obtained:
            break
    if obtained:
        break

for item in material_dict:
    print(f"{item}: {material_dict[item]}")
