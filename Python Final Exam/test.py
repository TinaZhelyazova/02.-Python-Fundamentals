dictionary = {}
number = int(input())

for i in range(number):
    word = input()
    synonym = input()

    if word not in dictionary.keys():
        dictionary[word] = []
    dictionary[word].append(synonym)

data = [f"{key} - {', '.join(value)}" for key, value in dictionary.items()]
print("\n".join(data))


"""from collections import deque

queue = deque([2, 4, 6])
queue.append(5)
queue.appendleft(3)
print(queue)
queue.pop()
print(queue)
queue.append(3)
queue.popleft()
print(queue)
"""