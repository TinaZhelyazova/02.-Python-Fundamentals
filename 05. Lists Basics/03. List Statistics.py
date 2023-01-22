n = int(input())
positive_numbers_list = []
negative_numbers_list = []

for i in range(n):
    curr_number = int(input())
    if curr_number >= 0:
        positive_numbers_list.append(curr_number)
    else:
        negative_numbers_list.append(curr_number)

print(positive_numbers_list)
print(negative_numbers_list)
print(f"Count of positives: {len(positive_numbers_list)}")
print(f"Sum of negatives: {sum(negative_numbers_list)}")
