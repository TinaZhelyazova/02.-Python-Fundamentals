notebook = {}
words = input().split(" | ")
for i in words:
    word, definition = i.split(": ")
    if word in notebook:
        notebook[word].append(definition)
    else:
        notebook[word] = [definition]
test_words = input().split(" | ")
command = input()

if command == "Test":
    for word in test_words:
        if word in notebook:
            print(f"{word}:")
            for definition in notebook[word]:
                print(f" -{definition}")
else:
    print(" ".join(notebook.keys()))
