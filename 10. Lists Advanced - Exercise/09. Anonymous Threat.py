input_text = input().split(" ")
concatenated_data = ""
divided_data = []

while True:
    text = input().split(" ")
    command = text[0]
    el_parts = []

    if text[0] == "3:1":
        break

    if command == "merge":
        start_index = int(text[1])
        end_index = int(text[2])

        start_index = max(0, start_index)
        end_index = min(len(input_text) - 1, end_index)
        range_of_concatenation = abs(end_index - start_index + 1)

        if start_index >= end_index:
            continue

        for i in range(range_of_concatenation):
            concatenated_data += input_text[start_index]
            input_text.pop(start_index)

        input_text.insert(start_index, concatenated_data)
        concatenated_data = ""

    if command == "divide":
        index = int(text[1])
        partitions = int(text[2]) #на колко части ще разделим думата
        word = input_text[index]
        division = len(input_text[index]) // partitions # на колко букви ще разделим думата

        split_word = ""
        for partition in range((partitions - 1) * division):
            split_word += word[index]
            if len(split_word) == division:
                el_parts.append(split_word)
                split_word = ""

        split_word = ""
        for idx in range((partitions - 1)*division, len(word)):
            split_word +=word[index]

        el_parts.append(split_word)

        input_text.pop(index)
        for i in range(len(el_parts)):
            input_text.insert(index + i)

print(" ".join(input_text))
