a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

if a[0] == b[0] == c[0] or a[0] == a[1] == a[2]:
    winner = a[0]
    if a[0] == 0:
        print("Draw!")
    elif a[0] == 1:
        print("First player won")
    else:
        print("Second player won")
elif a[1] == b[1] == c[1] or b[0] == b[1] == b[2]:
    winner = b[1]
    if b[1] == 0:
        print("Draw!")
    elif b[1] == 1:
        print("First player won")
    else:
        print("Second player won")
elif a[2] == b[2] == c[2] or c[0] == c[1] == c[2]:
    winner = c[2]
    if c[2] == 0:
        print("Draw!")
    elif c[2] == 1:
        print("First player won")
    else:
        print("Second player won")
elif a[0] == b[1] == c[2] or a[2] == b[1] == c[0]:
    winner = b[1]
    if b[1] == 0:
        print("Draw!")
    elif b[1] == 1:
        print("First player won")
    else:
        print("Second player won")
else:
    print("Draw!")
