synonym_dict = {}
number = int(input())

for i in range(number):
    word = input()
    synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = []
        synonym_dict[word].append(synonym)
    else:
        synonym_dict[word].append(synonym)

for (key, value) in synonym_dict.items():
    print(f'{key} - {", ".join(value)}')
