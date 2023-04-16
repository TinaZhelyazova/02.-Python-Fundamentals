country_names = input().split(", ")
capital_cities = input().split(", ")
countries = {country_names[i]: capital_cities[i] for i in range(len(country_names))}

for key,value in countries.items():
    print(f"{key} -> {value}")
