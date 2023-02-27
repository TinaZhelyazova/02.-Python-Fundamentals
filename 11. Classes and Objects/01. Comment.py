class Comment:
    def __init__(self, username, content):
        self.username = username
        self.content = content
        self.likes = 0


name = input()
cont = input()
obj = Comment(name, cont)
print(obj.username)
print(obj.content)
print(obj.likes)

