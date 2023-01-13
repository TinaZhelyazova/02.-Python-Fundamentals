string_one = input()
string_two = input()
new_string = string_one

for i in range(len(string_one)):
    left_part = string_two[:i+1]
    right_part = string_one[i+1:]
    current_string = left_part+right_part
    if current_string == new_string:
        continue
    print(current_string)
    new_string = current_string