dict = {}

for i in range(5):
    names_ages = input().split(" ")
    name = names_ages[0]
    age = names_ages[1]
    if name not in dict:
        dict[name] = []
    dict[name].append(age)

    for ages in dict.values():
        if age not in ages:
            print("yes")
        else:
            print("no")


    #print(dict)


#tania 20
#yoana 30
#tania 40
#radi 32
#asfd 45